import ListaBaseDatos as Storage
import os
import re

storage = Storage.ListaBaseDatos()
main_path = os.getcwd()+"\\data"
db_name_pattern = "^[a-zA-Z_].*"

# Cambiar la ubicación del directorio data (por defecto se usará el directorio de consola)


def setDir(newPath: str):

    global main_path
    temp_path = newPath+"\\data"

    try:

        if os.path.isdir(newPath):

            if not os.path.isdir(temp_path):
                os.mkdir(temp_path)

            main_path = temp_path
            Storage.main_path = temp_path

            __init__()
        
        else:
            print("'"+newPath+"' no es un directorio valido")

    except os.error:
        print(os.error)

# ==//== funciones con respecto a ListaBaseDatos ==//==
# Se llama la función sobre la clase ListaBaseDatos


def createDatabase(mode: int, databaseName: str):

    if re.search(db_name_pattern, databaseName):

        if mode in range(1, 6):
            return storage.createDatabase(5, databaseName)

        else:
            return 3

    else:
        return 2


def showDatabases():

    return storage.showDatabases()


def alterDatabase(databaseOld: str, databaseNew: str):

    if re.search(db_name_pattern, databaseOld) and re.search(db_name_pattern, databaseNew):
        return storage.alterDatabase(databaseOld, databaseNew)

    else:
        return False


def dropDatabase(databaseName: str):

    if databaseName:
        return storage.dropDatabase(databaseName)

    else:
        print("Se necesita un nombre para la base de datos")
        return 1


# ==//== funciones con respecto a BaseDatos ==//==
# Primero se busca la base de datos y luego se llama la función sobre la clase BaseDatos

def createTable(databaseName, tableName, numberColumns):

    temp = storage.Buscar(databaseName)

    if temp:
        return temp.createTable(tableName, numberColumns)

    else:
        print("Base de datos '"+databaseName+"' no encontrada")
        return 1


def showTables(databaseName):

    temp = storage.Buscar(databaseName)

    if temp:
        return temp.showTables()

    else:
        print("Base de datos '"+databaseName+"' no encontrada")
        return 1


def alterTable(databaseName, tableOld, tableNew):

    temp = storage.Buscar(databaseName)

    if temp:
        return temp.alterTable(tableOld, tableNew)

    else:
        print("Base de datos '"+databaseName+"' no encontrada")
        return 1


def dropTable(databaseName, tableName):

    temp = storage.Buscar(databaseName)

    if temp:
        return temp.dropTable(tableName)

    else:
        print("Base de datos '"+databaseName+"' no encontrada")
        return 1


def alterAdd(databaseName, tableName, columnName):

    temp = storage.Buscar(databaseName)

    if temp:
        return temp.alterAdd(tableName, columnName)

    else:
        print("Base de datos '"+databaseName+"' no encontrada")
        return 1


def alterDrop(databaseName, tableName, columnName):

    temp = storage.Buscar(databaseName)

    if temp:
        return temp.alterDrop(tableName, columnName)

    else:
        print("Base de datos '"+databaseName+"' no encontrada")
        return 1


def extractTable(databaseName, tableName):

    temp = storage.Buscar(databaseName)

    if temp:
        return temp.extractTable(tableName)

    else:
        print("Base de datos '"+databaseName+"' no encontrada")
        return 1


# ==//== funciones con respecto a Tabla ==//==
# Primero se busca la base de datos, luego la tabla, y luego se llama la función sobre la clase Tabla

def insert(databaseName, tableName, columns):

    temp = storage.Buscar(databaseName)

    if temp:

        temp = temp.Buscar(tableName)

        if temp:
            return temp.insertar(columns)

        else:
            print("Tabla '"+tableName+"' no creada")

    else:
        print("Base de datos '"+databaseName+"' no encontrada")
        return 1


def update(databaseName, tableName, id, columnNumber, value):

    temp = storage.Buscar(databaseName)

    if temp:

        temp = temp.Buscar(tableName)

        if temp:
            return temp.update(id, columnNumber, value)

        else:
            print("Tabla '"+tableName+"' no creada")

    else:
        print("Base de datos '"+databaseName+"' no encontrada")
        return 1


def deleteTable(databaseName, tableName, id):

    temp = storage.Buscar(databaseName)

    if temp:

        temp = temp.Buscar(tableName)

        if temp:
            return temp.deleteTable(id)

        else:
            print("Tabla '"+tableName+"' no creada")

    else:
        print("Base de datos '"+databaseName+"' no encontrada")
        return 1


def truncate(databaseName, tableName):

    temp = storage.Buscar(databaseName)

    if temp:

        temp = temp.Buscar(tableName)

        if temp:
            return temp.truncate()

        else:
            print("Tabla '"+tableName+"' no creada")

    else:
        print("Base de datos '"+databaseName+"' no encontrada")
        return 1


def extractRow(databaseName, tableName, id):

    temp = storage.Buscar(databaseName)

    if temp:

        temp = temp.Buscar(tableName)

        if temp:
            return temp.extractRow(id)

        else:
            print("Tabla '"+tableName+"' no creada")

    else:
        print("Base de datos '"+databaseName+"' no encontrada")
        return 1


# ==//== carga de tabla mediante archivo CSV ==//==

def loadCSV(filecsv, databaseName, tableName, numberColumns):

    try:
        archivo = open(filecsv)

    except:
        print("No se encontró el archivo del CSV")
        return 1

    database_temp = storage.Buscar(databaseName)
    table_temp = storage.Buscar(databaseName).Buscar(tableName)

    if not database_temp:
        createDatabase(5, databaseName)

    if not table_temp:
        createTable(databaseName, tableName, numberColumns)

    elif table_temp.tamano != numberColumns:
        print("no coinciden")
        return 1

    header = archivo.readline().replace("\n", "").split(",")
    temp_registros = archivo.readlines()

    registros = []

    for registro in temp_registros:
        registros.append(registro.replace("\n", "").split(","))

    # insertar

    print(header)
    print(registros)
    return 0


# ==//== inicialización del sistema de directorios ==//==

def __init__():

    if os.path.isdir(main_path):

        for db in os.listdir(main_path):
            storage.createDatabase(5, db)

    else:
        os.mkdir(main_path)

    #print(">> Se cargaron:")
    showDatabases()


__init__()
