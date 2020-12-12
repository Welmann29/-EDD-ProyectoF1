import BaseDatos as DB
import os

main_path = os.getcwd()+"\\data\\hash"


class ListaBaseDatos:

    def __init__(self):

        self.lista_bases_datos = []
        

    def Buscar(self, database):

        for base_datos in self.lista_bases_datos:

            if base_datos.Name == database:
                return base_datos

        else:
            return False


    def createDatabase(self, database):

        for base_datos in self.lista_bases_datos:

            if base_datos.Name == database:
                return 2

        else:
            temp_path = main_path+"\\"+database

            if not os.path.isdir(temp_path):
                os.mkdir(temp_path)

            temp = DB.BaseDatos(database, temp_path)          
            self.lista_bases_datos.append(temp)
                
            return 0


    def showDatabases(self):
        
        temp_list = []

        for base_datos in self.lista_bases_datos:
            temp_list.append(base_datos.Name)

        self.graficar()
        return temp_list


    def alterDatabase(self, databaseOld, databaseNew):

        temp_old = self.Buscar(databaseOld)
        temp_new = self.Buscar(databaseNew)

        if temp_old:

            if not temp_new:
                temp_old.Name = databaseNew

                temp_path_old = main_path+"\\"+databaseOld
                temp_path_new = main_path+"\\"+databaseNew

                os.rename(temp_path_old, temp_path_new)

                return 0

            else:
                return 3

        else:
            return 2


    def dropDatabase(self, database):

        temp = self.Buscar(database)

        if temp:
            self.lista_bases_datos.remove(temp)

            temp_path = main_path+"\\"+database

            if os.path.isdir(temp_path):
                os.rmdir(temp_path)

            return 0

        else:
            return 2


    def graficar(self):
        print("si")
        file = open('bases_de_datos.dot', "w")
        file.write("digraph grafica{" + os.linesep)
        file.write("rankdir=LR;" + os.linesep)

        info = "<<table><tr>"
        for i in self.lista_bases_datos:
            info += "<td>"+i.Name+"</td>"
        info += "</tr></table>>"

        file.write(info)
        file.write(' }' + os.linesep)
        file.close()
        os.system('dot -Tpng bases_de_datos.dot -o bases_de_datos.png')
        os.system('bases_de_datos.png')
        print("siii")
