import BaseDatos as DB

class ListaBaseDatos:

    def __init__(self):

        self.lista_bases_datos=[]


    def Buscar(self, databaseName):

        for base_datos in self.lista_bases_datos:

            if base_datos.Name==databaseName:
                return base_datos

        else: 
            return False
            

    def createDatabase(self, databaseName):

        for base_datos in self.lista_bases_datos:

            if base_datos.Name==databaseName:
                print("Base de datos '"+databaseName+"' ya existente, no se pudo crear")
                return

        else:
            db=DB.BaseDatos(databaseName)
            self.lista_bases_datos.append(db)
            print("Base de datos '"+databaseName+"' creada con éxito")


    def showDatabases(self):

        print("//==============================//")
        print(" - -   BD EN ALMACENAMIENTO   - -")

        for base_datos in self.lista_bases_datos:
            print(base_datos.Name)
        
        print("//==============================//")


    def alterDatabase(self, databaseOld, databaseNew):

        temp=self.Buscar(databaseOld)

        if temp:
            temp.Name=databaseNew
            print("Base de datos '"+databaseOld+"' renombrada a '"+databaseNew+"'")

        else:            
            print("Base de datos '"+databaseOld+"' no encontrada")


    def dropDatabase(self, databaseName):

        temp=self.Buscar(databaseName)

        if temp:
            self.lista_bases_datos.remove(temp)
            print("Base de datos '"+databaseName+"' eliminada con éxito")

        else:
            print("Base de datos '"+databaseName+"' no encontrada")
