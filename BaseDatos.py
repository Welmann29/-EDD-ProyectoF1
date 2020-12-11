import Tabla

class BaseDatos:
    def __init__(self, Name):
        self.Name = Name
        self.list_table = []


    # == BUSCAR BASES DE DATOS
    def Buscar(self, table):
        salida = []
        existe = False
        col = 0
        i = 0
        for nombre in self.list_table:
            if nombre[0] == table:
                existe = True
                col = nombre[1]
                break
            else:
                existe = False
                i = i+1
        salida = [existe, i, col]
        return salida


    # == CREAR TABLAS

    def createTable(self, tableName, numberColumns):
        salida = []
        if len(self.list_table) == 0:
            self.list_table.append([tableName, numberColumns])
            existe = True
        else:
            salida = self.Buscar(tableName)
            existe = salida[0]
            if existe == False:
                self.list_table.append([tableName, numberColumns])
            
    # == MOSTRAR TABLAS
    def showTables(self):
        nombre = []
        for n in self.list_table:
            nombre.append(n[0])
        print(nombre)

    # == CAMBIAR NOMBRES
    def alterTable(self, tableOld, tableNew):
        salida = self.Buscar(tableOld)
        if salida[0]:
            self.list_table[salida[1]][0]= tableNew
        else:
            return 1
    
    # === ELIMINAR TABLA
    def dropTable(self,tableName):
        salida = self.Buscar(tableName)
        if salida[0]:
            self.list_table.pop(salida[1])
        else:
            return 1

    # === alterAdd

    # === alterDrop

    # === extractTable 276

B = BaseDatos('Alejandra')
B.createTable('Ale',10)
B.createTable('Marcos',5)
B.createTable('Alejandro',20)
B.createTable('Ale',1)
B.createTable('Navarro',7)
B.showTables()
B.dropTable('Ale')
B.showTables()
B.createTable('YaFeliz:)',7)
B.showTables()
B.alterTable('Navarro','AleFeliz')
B.showTables()