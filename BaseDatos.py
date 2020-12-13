import Tabla
import serealizar
import os

class BaseDatos:
    def __init__(self, Name, main_path):
        self.Name = Name
        self.list_table = []
        self.main_path = main_path
        for tabla in os.listdir(self.main_path):
            temp = tabla.replace(".bin","")
            self.list_table.append(temp)


    # == BUSCAR TABLA
    def Buscar(self, table):
        existe = False
        i = 0
        if table in self.list_table:
            existe = True
        else:
            existe = False
            i = i+1
        salida = [existe, i]
        return salida


    # == CREAR TABLAS
    def createTable(self, tableName, numberColumns):
        if not tableName in self.list_table:
            self.list_table.append(tableName)
            temp = Tabla.Tabla(tableName, numberColumns)
            serealizar.commit(temp, tableName, self.main_path)

            return 0

        else:
            return 3


    # == CREAR LLAVES PRIMARIAS Y FORÁNEAS                
    def definePK(self, table, columns):

        # codigo para cambiar la lista de PK de una tabla dada
        return 0 #operacion exitosa

    def defineFK(self):
        #codigo en proceso (FASE 2)
        pass


    # == MOSTRAR TABLAS
    def showTables(self):
        return self.list_table

    # == CAMBIAR NOMBRES
    def alterTable(self, tableOld, tableNew):
        temp = serealizar.rollback(tableOld, self.main_path)
        os.remove(self.main_path+"\\"+tableOld+".bin")
        salida = self.Buscar(tableOld)
        if salida[0]:
            if not tableNew in self.list_table:
                self.list_table[salida[1]]= tableNew
                temp.alterTable(tableNew)
                serealizar.commit(temp, tableNew, self.main_path)
                return 0
            else:
                return 4
        else:
            return 3
    
    # === ELIMINAR TABLA
    def dropTable(self,tableName):
        salida = self.Buscar(tableName)
        if salida[0]:
            self.list_table.pop(salida[1])
            os.remove(self.main_path+"\\"+tableName+".bin")
            return 0
        else:
            return 3

    # === AGREGAR N-ESIMA COLUMNA
    def alterAddColumn(self, table):
        salida = self.Buscar(table)
        if salida[0]:
            temp = serealizar.rollback(table, self.main_path)
            temp.alterAddColumn()
            serealizar.commit(temp, table, self.main_path)
            return 0
        else:
            return 3

    # === ELIMINAR N-ESIMA COLUMNA
    def alterDropColumn(self, table, columnNumber):
        salida = self.Buscar(table)
        if salida[0]:
            temp = serealizar.rollback(table, self.main_path)
            temp.alterDropColumn(columnNumber)
            serealizar.commit(temp, table, self.main_path)
            return 0
        else:
            return 3

    # === EXTRAER INFORMACIÓN
    def extractTable(self, table):
        if table in self.list_table:
            temp = serealizar.rollback(table, self.main_path)
            return temp.extractTable()
        else:
            return None
            
    def extractRangeTable(self, table, lower, upper):
        if table in self.list_table:
            temp = serealizar.rollback(table, self.main_path)
            return temp.extractRangeTable(lower, upper)
            #implementar en la clase Tabla
        else:
            return None
    
    # === GRAFICAR LAS TABLAS QUE CONTIENE LA BD
    def graficar(self):
        file = open('tablas.dot', "w")
        file.write("digraph grafica{" + os.linesep)
        file.write("rankdir=LR;" + os.linesep)

        info = "<<table><tr>"
        for i in self.list_table:
            info += "<td>"+i+"</td>"
        info += "</tr></table>>"

        file.write(' }' + os.linesep)
        file.close()
        os.system('dot -Tpng tablas.dot -o tablas.png')
        os.system('tablas.png')