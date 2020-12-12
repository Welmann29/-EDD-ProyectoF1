import Tabla
import serealizar
import os

class BaseDatos:
    def __init__(self, Name, directorio):
        self.Name = Name
        self.list_table = []
        self.directorio = directorio
        for tabla in os.listdir(self.directorio):
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
            serealizar.commit(temp, tableName, self.directorio)
                    
    # == MOSTRAR TABLAS
    def showTables(self):
        return self.list_table

    # == CAMBIAR NOMBRES
    def alterTable(self, tableOld, tableNew):
        temp = serealizar.rollback(tableOld, self.directorio)
        os.remove(self.directorio+"\\"+tableOld+".bin")
        salida = self.Buscar(tableOld)
        if salida[0]:
            if not tableNew in self.list_table:
                self.list_table[salida[1]]= tableNew
                temp.alterTable(tableNew)
                serealizar.commit(temp, tableNew, self.directorio)
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
            os.remove(self.directorio+"\\"+tableName+".bin")
            return 0
        else:
            return 3

    # === AGREGAR N-ESIMA COLUMNA
    def alterAddColumn(self, table):
        salida = self.Buscar(table)
        if salida[0]:
            temp = serealizar.rollback(table, self.directorio)
            temp.alterAddColumn()
            serealizar.commit(temp, table, self.directorio)
            return 0
        else:
            return 3

    # === ELIMINAR N-ESIMA COLUMNA
    def alterDropColumn(self, table, columnNumber):
        salida = self.Buscar(table)
        if salida[0]:
            temp = serealizar.rollback(table, self.directorio)
            temp.alterDropColumn(columnNumber)
            serealizar.commit(temp, table, self.directorio)
            return 0
        else:
            return 3

    # === EXTRAER INFORMACIÓN
    def extractTable(self, table):
        if table in self.list_table:
            temp = serealizar.rollback(table, self.directorio)
            return temp.extractTable()
    
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