# Manual De Usuario

HashMode es una librería escrita en Python 3 que provee almacenamiento para un administrador de bases de datos (DBMS). HashMode almacena datos localmente utilizando tablas de dispersión (tablas hash).

## Indice

- [Glosario](#glosario)
- [FAQ](#faq)
- [Uso del reportador gráfico](#uso-del-reportador-gráfico)
- [Uso de la librería](#uso-de-la-librería)
- [Uso de funciones de bases de datos](#uso-de-funciones-de-bases-de-datos)
- [Uso de funciones de tablas](#uso-de-funciones-de-tablas)
- [Uso de funciones de registros](#uso-de-funciones-de-registros)


## Glosario

cuerpo

## FAQ

cuerpo

## Uso de la librería

Para ejecutar la librería es necesario tener instalado Python 3 para [Windows](https://www.python.org/downloads/windows/) o para [Linux](https://www.python.org/downloads/source/).

HashMode se puede incorporar en un proyecto con la siguiente línea de código:

```sh
import HashMode
```

Se puede acceder al repertorio de funciones posteriormente descritas de la siguiente manera:

```sh
HashMode.createDatabase("new_database")
HashMode.showDatabases()
...
```

HashMode almacena todo dentro de la carpeta *data/hash* del proyecto, de manera recurrente y eficaz. Esta ubicación puede ser cambiada mediante:

```sh
setDir("new_path")
```

## Uso del reportador gráfico

cuerpo

## Uso de funciones de bases de datos

Las siguientes funciones se enfocan en la manipulación de bases de datos.

### createDatabase(database)

Crea una base de datos, dentro de la cual se pueden almacenar tablas. El parametro *database* se refiere al nombre que tendrá la base de datos. El contenido de la base de datos se almacenará dentro de *data/hash/**database***. El nombre de la base de datos debe ser un identificador SQL válido.

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Nombre de la base de datos ocupado |

### showDatabases()

Despliega las bases de datos almacenadas en *data/hash*. 

| Valor de retorno | Definición |
| ------ | ------ |
| <lista> | Operación exitosa |
| <lista vacía> | No hay bases de datos almacenadas |
  
### alterDatabase(databaseOld, databaseNew)

Cambia el nombre de una base de datos almacenada. El parámetro *databaseOld* se refiere al nombre de origen, y *databaseNew* se refiere al nuevo nombre de la base de datos. El nuevo nombre de la base de datos debe ser un identificador SQL válido.

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos origen inexistente |
| 3 | Nuevo nombre de la base de datos ocupado |

### dropDatabase(database)

Elimina una base de datos con todo su contenido. El parámetro *database* se refiere al nombre de la base de datos que se desea eliminar. Esta operación no puede ser deshecha.

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |

## Uso de funciones de tablas

Las siguientes funciones se enfocan en la manipulación de las tablas de una base de datos previamente definida.

### createTable(database, table, numberColumns)

Crea una tabla en la base de datos especificada. Recibe tres parámetros, los cuales son: la base de datos donde creará la tabla, el nombre de la tabla a crear y el número de columnas que tendrá la misma. No pueden existir dos tablas con el mismo nombre en la misma base de datos.

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla existente |

### showTables(database)
Recopila las tablas que contiene la base de datos consultada y devuelve los nombre de las tablas en una lista.

| Valor de retorno | Definición |
| ------ | ------ |
| <Lista> | Operación exitosa |
| <Lista vacía> | La base de datos no contiene tablas |
| None | Base de datos inexistente |

### extractTable(database, table)
Extrae los registros que contiene una tabla. Recibe dos parámetros: la base de datos seleccionada y el nombre de la tabla a la cual se extraerán sus registros. Reenvía los parametros a la sección de registros.

| Valor de retorno | Definición |
| ------ | ------ |
| <Lista> | Operación exitosa |
| <Lista vacía> | La tabla no contiene registros |
| None | Error en la operación |

### extractRangeTable(database, table, columnNumber, lower, upper)
Extrae los registros correspondientes a un rango solicitado, para devolverlos en una lista. Reenvía los parametros a la sección de registros.

| Valor de retorno | Definición |
| ------ | ------ |
| <Lista> | Operación exitosa |
| <Lista vacía> | La tabla no contiene registros |
| None | Error en la operación |

### alterAddPK(database, table, columns) 
Asocia una llave primaria simple o compuesta a una tabla especificada. Reenvía los parametros a la sección de registros.

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla inexistente |
| 4 | Llave primaria existente |
| 5 | Columnas fuera de límites |

### alterDropPK(database, table)
Elimina la llave primaria actual en la tabla especificada. Reenvía los parámetros a la sección de registros.

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla inexistente |
| 4 | Llave primaria inexistente |

### alterTable(database, tableOld, tableNew)
Renombra la tabla que se especifique. Recibe 3 parámetros:  Nombre de la base de datos a acceder, el nombre actual de la tabla y el nuevo nombre que tomará.

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla a modificar inexistente |
| 4 | Nuevo nombre de tabla existente |

### alterAddColumn(database, table, default)
Agrega una columna más a la tabla especificada, el parámetro default es el valor que tomará la nueva columna. Reenvía los parámetros a la sección de registro.

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla inexistente |

### alterDropColumn(database, table, columnNumber)
Elimina la columna especificada con excepción que sean llaves primarias. Recibe 3 parámetros: Nombre de la base de datos a acceder, nombre de la tabla a modificar y numero de columna a eliminar. Reenvía los parámetros a la sección de registro.

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla inexistente |
| 4 | Es llave primaria o la tabla no puede quedarse sin columnas |
| 5 | Columna fuera de límites |

### dropTable(database, table)
Elimina una tabla de la base de datos especificada. Recibe dos parámetros: Nombre de la base de datos a acceder y nombre de la tabla a eliminar.

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla inexistente |


## Uso de funciones de tuplas

Las siguientes funciones se enfocan en la manipulación de las tuplas de una tabla previamente definida.

### insert(database, table, register)

Ingresa un nuevo registro en la tabla de la base de datos especificada. Recibe como parametro el nombre de la base de datos, de la tabla y una lista con los valores a insertar. Esta lista debe tener exactamente el numero de elementos correspondientes a el numero de columnas de la tabla especificada, si tiene columnas vacias, se sugiere que concatene None hasta completar el numero de elementos.

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla existente |
| 4 | Llave primaria duplicada |
| 5 | Numero de columnas no coinciden |

### extractRow(database, table, primaryKey[list])
Con esta funcion es posible extraer la informacion de una tupla especificando su llave primaria. Recibe como parametro el nombre de la base de datos, de la tabla y una lista con los valores que componen la llave primaria; si la llave primaria es simple, de igual manera se debe enviar en forma de lista; se sugiere que se envie todo dato entero en formato entero.

| Valor de retorno | Definición |
| ------ | ------ |
| Lista de datos | Operación exitosa |
| <Lista vacía> | Cualquier error en la operacion |


### update(database, table, dict, primaryKey[list])
Esta funcion permite modificar los datos de un registro en especifico, especificando su llave primaria, es posible modificar las propias llaves primarias, sin embargo se verificara que la nueva primaria no este repetida, esto para mantener la consistencia de los datos, si la nueva primaria se repite la operacion fallara. Recibe como parametro el nombre de la base de datos, de la tabla, una lista con los valores que componen la llave primaria; si la llave primaria es simple, de igual manera se debe enviar en forma de lista; y un diccionario que tenga como claves la columna a modificar y como valor el nuevo valor a modificar, se sugiere que se envie todo dato entero en formato entero.

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla existente |
| 4 | Llave primaria no existe |

### delete(database, table, columnNumber, primaryKey[list])
Elimina totalmente un registro de la tabla especificada por medio de su llave primaria. Recibe como parametro el nombre de la base de datos, de la tabla y una lista con los valores que componen la llave primaria; si la llave primaria es simple, de igual manera se debe enviar en forma de lista; se sugiere que se envie todo dato entero en formato entero.

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla existente |
| 4 | Llave primaria no existe |

### truncate(database, table) 
Vacia una tabla, dejandola sin registros pero sin eliminarla totalmente de la base de datos. Recibe como parametro el nombre de la base de datos y de la tabla a vacear.

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla inexistente |


### loadCSV(file, database, table)
Inserta los registros descritos en un documento *file* (.csv) en una tabla dada por el parámetro *table*, dentro de la base de datos dada por el parámetro *database*.

La función puede retornar los siguientes valores una vez.

| Valor de retorno | Definición |
| ------ | ------ |
| <Lista vacía> | Error en la operación / Base de datos inexistente / Tabla inexistente |

O también puede retornar los siguientes valores tantas veces como registros hayan en el archivo *csv*.

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 4 | Llave primaria duplicada |
| 5 | Base de datos inexistente |
