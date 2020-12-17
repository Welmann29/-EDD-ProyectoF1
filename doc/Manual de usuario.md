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
| <lista de bases de datos> | Operación exitosa |
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

cuerpo

## Uso de funciones de registros

cuerpo


### loadCSV(file, database, table)
Inserta los registros descritos en un documento *file* (.csv) en una tabla dada por el parámetro *table*, dentro de la base de datos dada por el parámetro *database*.

La función puede retornar los siguientes valores una vez.

| Valor de retorno | Definición |
| ------ | ------ |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla inexistente |

O también puede retornar los siguientes valores tantas veces como registros hayan en el archivo *csv*.

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 4 | Llave primaria duplicada |
| 5 | Base de datos inexistente |
