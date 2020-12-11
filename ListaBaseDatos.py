import BaseDatos as DB
import os

main_path = os.getcwd()+"\\data"


class ListaBaseDatos:

    def __init__(self):

        self.lista_bases_datos = []

    def Buscar(self, databaseName):

        for base_datos in self.lista_bases_datos:

            if base_datos.Name == databaseName:
                return base_datos

        else:
            return False

    def createDatabase(self, mode, databaseName):

        for base_datos in self.lista_bases_datos:

            if base_datos.Name == databaseName:
                return 1

        else:
            self.lista_bases_datos.append(DB.BaseDatos(databaseName))

            temp_path = main_path+"\\"+databaseName

            if not os.path.isdir(temp_path): #######
                os.mkdir(temp_path)
                
            return 0

    def showDatabases(self):
        
        print("DB ALMACENADAS:")
        print("//==============================//")
        print(" - -            BD            - -")

        temp_list = []

        for base_datos in self.lista_bases_datos:
            temp_list.append(base_datos.Name)
            print(base_datos.Name)

        print("//==============================//")

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

                print("Base de datos '"+databaseOld +
                      "' renombrada a '"+databaseNew+"'")
                return True

            else:
                print("Base de datos '"+databaseNew+"' ya existente")
                return False

        else:
            print("Base de datos '"+databaseOld+"' no encontrada")
            return False

    def dropDatabase(self, databaseName):

        temp = self.Buscar(databaseName)

        if temp:
            self.lista_bases_datos.remove(temp)

            temp_path = main_path+"\\"+databaseName

            if os.path.isdir(temp_path):
                os.rmdir(temp_path)

            print("Base de datos '"+databaseName+"' eliminada con éxito")
            return 0

        else:
            print("Base de datos '"+databaseName+"' no encontrada")
            return 2
