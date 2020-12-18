# Manual Técnico

## Indice

- [Introducción](#introducción)
- [Objetivos](#objetivos)
- [Alcances del proyecto](#alcances-del-proyecto)
- [Requerimentos funcionales](#requerimentos-funcionales)
- [Estructura de bases de datos](#estructura-de-bases-de-datos)
- [Estructura de tablas](#estructura-de-tablas)
- [Estructura de registros](#estructura-de-registros)
- [Reportador gráfico](#reportador-grafico)
- [Diagrama de clases](#diagrama-de-clases)
- [Diagrama de Gantt](#diagrama-de-gantt)

## Introducción

cuerpo

## Objetivos

cuerpo

## Alcances del proyecto

Este proyecto esta focalizado a la creación de la estructura interna de un Sistema Manejador de Bases de Datos, o DataBase Management System (DBMS). Se podría calificar como un subproyecto, de un proyecto que se trabaja en conjunto a compañeros de otros dos cursos de la carrera de Ingenieria en Ciencias y Sistemas en la Universidad de San Carlos de Guatemala, siendo la idea primordial, la unificación de los 3 proyectos, para la creación de un DBMS completo y funcional, creado desde cero, y con licencia abierta MIT.

Esta siendo elaborado por estudiantes del curso Estructuras de Datos, por lo cual consiste en una librería que provee funciones para crear, modificar y eliminar bases de datos, tablas y sus registros.  

El modo de almacenamiento que maneja esta librería es por medio de tablas Hash, de ahí el nombre HashMode, la estructura propuesta se utiliza en las tablas, es decir cada tabla se maneja como una Tabla Hash en la cual se almacenan los registros o tuplas, el acceso al almacenamiento es por medio de la llave primaria previamente definida para la tabla en cuestión, o bien, con una llave escondida en caso que no se defina llave primaria.

La finalidad de utilizar las tablas Hash como modo de almacenamiento es para explotar su orden de complejidad, en la búsqueda de los datos, siendo esta en el mejor de los casos un orden constante O(1), puesto que con la función hash se puede obtener directamente el índice en el cual se encuentra almacenado el dato al que queremos acceder. 

Se utiliza una Tabla Hash abierta de direccionamiento cerrado, se eligió esta, sobre la tabla cerrada de direccionamiento abierto, pues se exploro una forma de explotar la característica de enlistar los datos que van al mismo índice (conocidos como colisiones), pues esta lista es manipulable y se pueden explorar algoritmos de búsqueda mas rápidos, situación que se vuelve complicada en las tablas de direccionamiento abierto, pues en ellas no se conoce con exactitud donde pueden ubicarse los datos que colisionan, creando una complejidad lineal O(n) en el acceso a los datos, sin embargo las cuestiones técnicas de la elección de la estructura se abordan en la sección [Estructura de tablas](#estructura-de-tablas).

No todo se maneja con tablas Hash, puesto que se considero que la parte con mas volumen de datos a manejar son las tablas, sin embargo, las bases de datos se manejan como listas sencillas de Python, pues no se esperan cantidades excesivas de tablas en una base de datos, así mismo la lista que almacena las bases de datos es una lista sencilla de Python. 

Como estructura interna de un DBMS, además de la eficiencia y eficacia de las creaciones, inserciones y demás gestiones, otro punto importante es la persistencia de los datos, dicha persistencia se maneja con un sistema hibrido entre un sistema jerárquico de ficheros y la serialización de objetos que guardan la información de cada Tabla Hash, así cada vez que se insertan nuevos registros los cambios se guardan en memoria volviendo a serializar los objetos previamente creados, este proceso de recuperar y serializar los objetos puede ser significativo para la maquina y la eficiencia del proyecto, es por ello que se recurrió a algoritmos que hicieran menos recurrente este proceso y se aprovecharan también los recursos cargados en memoria en cierto instante de la ejecución de la librería, esto hace más eficaz las operaciones aunque exige un poco de persistencia en memoria de cierto objetos, siempre respetando limites para no sobrecargarla de información.


## Requerimentos funcionales

cuerpo

## Estructura de bases de datos

cuerpo

## Estructura de tablas

cuerpo

## Estructura de registros

cuerpo

## Reportador gráfico

cuerpo

## Diagrama de clases

![diagrama-clases](img/diagrama-clases.png "Diagrama de clases")

## Diagrama de Gantt

cuerpo
