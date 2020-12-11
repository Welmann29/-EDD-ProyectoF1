import os
import subprocess
import time
import random

class Nodo(object):
    def __init__(self, datos):
        self.datos = datos
        self.primaria = datos[0]
        if type(self.primaria) is str:
            self.tipo = 'str'
        else:
            self.tipo = 'int'


class Tabla(object):
    def __init__(self, nombre, columnas):
        self.nombre = nombre
        self.columnas = columnas
        self.vector = []
        self.tamano = 13
        self.elementos = 0
        self.factorCarga = 0
        self.tipoPrimaria = None
        for i in range(self.tamano):
            self.vector.append(None)

    '''
    En caso de que la llave primaria sea una cadena este metodo me devolvera un numerico para
    lograr indexarla
    '''

    def toASCII(self, cadena):
        result = 0
        for char in cadena:
            result += ord(char)
        return result

    '''
    Metodo correspondiente al metodo insert(database, table, columns)
    sin embargo desde a esta clase solo llega el columns, que es una lista de 
    datos
    '''

    def insertar(self, datos):
        if len(datos) == self.columnas:
            nuevo = Nodo(datos)
            if self.elementos == 0:
                self.tipoPrimaria = nuevo.tipo
            else:
                if self.tipoPrimaria != nuevo.tipo:
                    return False
            posicion = self.funcionHash(nuevo.primaria)
            # Ahora se verificara si la posicion ya tiene una lista o esta vacia
            if self.vector[posicion] is None:
                self.vector[posicion] = []
                self.vector[posicion].append(nuevo)
                self.elementos += 1
                return True

            '''
            Aqui se verifica que no existan valores repetidos ya que estamos hablando de llaves primarias,
            sin embargo se divide en caso de se primarias string o enteras 
            '''
            if self.tipoPrimaria == 'int':
                if self.Existe(self.vector[posicion], nuevo.primaria):
                    return False
            else:
                if self.ExisteToAscii(self.vector[posicion], nuevo.primaria):
                    return False

            self.vector[posicion].append(nuevo)  # Se agrega el dato a la lista

            '''
            Se va a verificar el tipo de ordenamiento, si sera por int o para string
            '''
            if self.tipoPrimaria == 'int':
                self.vector[posicion] = self.OrdenarBurbuja(self.vector[posicion])
            else:
                self.vector[posicion] = self.OrdenarBurbujaToAscii(self.vector[posicion])

            self.factorCarga = self.elementos / self.tamano

            if self.factorCarga > 0.8:
                self.rehashing()

            return True
        else:
            return False

    def rehashing(self):
        while not (self.factorCarga < 0.3):
            self.tamano += 1
            self.factorCarga = self.elementos / self.tamano

        lista = []
        for i in self.vector:
            if i is None:
                '''No hace nada'''
            else:
                for j in i:
                    lista.append(j)

        self.vector = []
        for tamaño in range(self.tamano):
            self.vector.append(None)

        for nodo in lista:
            self.insertar(nodo.datos)

    def funcionHash(self, primaria):
        if self.tipoPrimaria == 'str':
            primaria = self.toASCII(primaria)
        index = primaria % self.tamano
        return index

    def imprimir(self):
        indice = 0
        print('Contenido de la tabla:', self.nombre)
        for i in self.vector:
            if i is None:
                print('Indice:', indice, 'Contenido:', i)
            else:
                print('Indice:', indice, 'Contenido:', end=' ')
                for j in i:
                    print('{Primaria:', j.primaria, 'Tupla:', str(j.datos) + '}', end=' ')
                print('')
            indice += 1

    '''
    Para Hacer una  busqueda mas efectiva se implementara el algoritmo de busqueda binaria
    '''

    def Existe(self, lista, dato):
        if len(lista) == 0:
            return False
        else:
            medio = len(lista) // 2
            if lista[medio].primaria == dato:
                return True
            else:
                if dato < lista[medio].primaria:
                    return self.Existe(lista[:medio], dato)
                else:
                    return self.Existe(lista[medio + 1:], dato)

    def ExisteToAscii(self, lista, dato):
        for i in lista:
            if i.primaria == dato:
                return True
        return False

    def BuscandoNodoToAscii(self, lista, dato):
        for i in lista:
            if i.primaria == dato:
                return i
        return False

    '''
    Ordenamiento de la lista, el metodo a utilizar sera el ordenamiento de burbuja
    '''

    def OrdenarBurbuja(self, vector):
        for i in range(1, len(vector)):
            for j in range(0, len(vector) - 1):
                if vector[j].primaria > vector[j + 1].primaria:
                    aux = vector[j + 1]
                    vector[j + 1] = vector[j]
                    vector[j] = aux
        return vector

    def OrdenarBurbujaToAscii(self, vector):
        for i in range(1, len(vector)):
            for j in range(0, len(vector) - 1):
                if self.toASCII(vector[j].primaria) > self.toASCII(vector[j + 1].primaria):
                    aux = vector[j + 1]
                    vector[j + 1] = vector[j]
                    vector[j] = aux
        return vector

    def BusquedaBinariaDevlviendoNodo(self, lista, dato):
        if len(lista) == 0:
            return False
        else:
            medio = len(lista) // 2
            if lista[medio].primaria == dato:
                return lista[medio]
            else:
                if dato < lista[medio].primaria:
                    return self.BusquedaBinariaDevlviendoNodo(lista[:medio], dato)
                else:
                    return self.BusquedaBinariaDevlviendoNodo(lista[medio + 1:], dato)

    '''
    Retorna el nodo para mostrar la informacion
    Representa la funcion ExtractRow()
    '''

    def ExtraerTupla(self, primaria):
        if self.tipoPrimaria == 'int':
            if type(primaria) is str:
                return False
            indice = self.funcionHash(primaria)
            casilla = self.vector[indice]
            if casilla is None:
                return False
            nodo = self.BusquedaBinariaDevlviendoNodo(casilla, primaria)
        else:
            if type(primaria) is int:
                return False
            indice = self.funcionHash(primaria)
            casilla = self.vector[indice]
            if casilla is None:
                return False
            nodo = self.BuscandoNodoToAscii(casilla, primaria)

        if type(nodo) == bool:
            return False
        else:
            return nodo.datos

    '''
    Truncate, metodo para vaciar la tabla totalmente 
    '''

    def truncate(self):
        self.vector = []
        self.tamano = 13
        for i in range(self.tamano):
            self.vector.append(None)

    '''
    deleteTable, elimina un registro de la tabla
    '''

    def deleteTable(self, primaria):
        if (type(primaria) is str) or (type(primaria) is int):
            indice = self.funcionHash(primaria)
            if len(self.vector[indice]) <= 1:
                self.vector[indice] = None
                self.elementos -= 1
                return True
            nuevo = self._delete(self.vector[indice], primaria)
            if type(nuevo) == bool:
                return False
            else:
                self.vector[indice] = nuevo
                return True
        else:
            return False

    def _delete(self, lista, primaria):
        if self.tipoPrimaria == 'int':
            elemento = self.BusquedaBinariaDevlviendoNodo(lista, primaria)
            if type(elemento) == bool:
                return False
            else:
                lista.remove(elemento)
                return lista
        else:
            for i in lista:
                if i.primaria == primaria:
                    lista.remove(i)
                    return lista
            return False

    def update(self, primaria, numeroColumna, nuevoValor):
        if not (numeroColumna < self.columnas):  # Si el numero de columna es mayor a las definidas falla
            return False

        if self.tipoPrimaria == 'int':
            if not (type(primaria) is int):
                return False
            indice = self.funcionHash(primaria)
            if not self.Existe(self.vector[indice], primaria):
                return False
            elemento = self.BusquedaBinariaDevlviendoNodo(self.vector[indice], primaria)
            indiceInterno = self.vector[indice].index(elemento)
            elemento.datos[numeroColumna] = nuevoValor
            self.vector[indice][indiceInterno] = elemento
            return True
        else:
            if not (type(primaria) is str):
                return False
            indice = self.funcionHash(primaria)
            if not self.ExisteToAscii(self.vector[indice], primaria):
                return False
            elemento = self.BuscandoNodoToAscii(self.vector[indice], primaria)
            indiceInterno = self.vector[indice].index(elemento)
            elemento.datos[numeroColumna] = nuevoValor
            self.vector[indice][indiceInterno] = elemento
            return True

    def extractTable(self):
        lista = []
        for i in self.vector:
            if i is None:
                '''No hace nada'''
            else:
                for j in i:
                    lista.append(j)
        if len(lista) > 0:
            if self.tipoPrimaria == 'int':
                lista = self.OrdenarBurbuja(lista)
            else:
                lista = self.OrdenarBurbujaToAscii(lista)
            ListaDeListas = []
            for i in lista:
                ListaDeListas.append(i.datos)
            return ListaDeListas
        else:
            return []

    def alterTable(self, name):
        self.nombre = name

    def Grafico(self):
        file = open('hash.dot', "w")
        file.write("digraph grafica{" + os.linesep)
        file.write('graph [pad="0.5"];' + os.linesep)
        file.write("nodesep=.05;" + os.linesep)
        file.write("rankdir=LR;" + os.linesep)
        file.write("node [shape=record,width=.1,height=.1];" + os.linesep)

        for i in range(self.tamano):
            if i == 0:
                file.write('node0 [label = "<f0> 0|' + os.linesep)
            elif i == self.tamano-1:
                file.write('<f' + str(i) + '> ' + str(i) + '",height='+str(self.tamano/2)+', width=.8];' + os.linesep)
            else:
                file.write('<f' + str(i) + '> ' + str(i) + '|' + os.linesep)

        contador = 0
        for listaNodos in self.vector:
            if not listaNodos is None:
                for nodo in listaNodos:
                    file.write('node' + str(nodo.primaria) + '[label = "{<n> ' + str(nodo.primaria) + '| <p> }"];' + os.linesep)
                file.write('node0:f' + str(contador) + ' -> node'+str(listaNodos[0].primaria)+':n;' + os.linesep)
                if len(listaNodos) > 1:
                    for i in range(len(listaNodos)):
                        if not i == len(listaNodos)-1:
                            file.write('node'+str(listaNodos[i].primaria)+':p -> node'+str(listaNodos[i+1].primaria)+':n;' + os.linesep)

            else:
                file.write('nodeNone' + str(contador) + ' [shape=plaintext, label="None", width=0.5]' + os.linesep)
                file.write('node0:f' + str(contador) + ' -> nodeNone' + str(contador) + os.linesep)
            contador += 1

        file.write(' }' + os.linesep)
        file.close()
        subprocess.call('dot -Tpng hash.dot -o hash.png')
        os.system('hash.png')

lista = []
lista.append(Nodo([10, 'Welmann']))
lista.append(Nodo([1, 'Welmann']))
lista.append(Nodo([15, 'Welmann']))
lista.append(Nodo([129, 'Welmann']))
lista.append(Nodo([12, 'Welmann']))

for i in lista:
    print(i.primaria)

tabla = Tabla('Integrantes', 2)
tabla2 = Tabla('Integrantes2', 2)

tabla2.insertar(['aa', 'Dato1'])
tabla2.insertar(['aa', 'Dato1 Repetido'])
tabla2.insertar(['ab', 'Dato2'])
tabla2.insertar(['ba', 'Dato2 invertido'])
tabla2.insertar(['aab', 'Dato3'])
tabla2.insertar(['aba', 'Dato3 modificado'])
tabla2.insertar(['ac', 'Dato4'])
tabla2.insertar(['ad', 'Dato5'])
tabla2.insertar(['ae', 'Dato6'])
tabla2.insertar(['af', 'Dato7'])
tabla2.insertar(['aggg', 'Dato8'])
tabla2.insertar(['abc', 'Dato9'])
tabla2.insertar(['arr', 'Dato11'])
tabla2.insertar(['acc', 'Dato10'])

print(tabla2.extractTable())
tabla2.Grafico()


lista = tabla.OrdenarBurbuja(lista)

print(tabla.Existe(lista, 12))
print(tabla.Existe(lista, 15))
print(tabla.Existe(lista, 129))
print(tabla.Existe(lista, 14))

for i in lista:
    print(i.primaria)

tabla.insertar([65, 'Primer65'])
tabla.insertar([1, 'Welmann', 'Paniagua'])
tabla.insertar([2, 'Welmann1'])
tabla.insertar([3, 'unico 3'])
tabla.insertar([4, 'Welmann3'])
tabla.insertar([5, 'Welmann4'])
print(tabla.insertar([6, 'Welmann5']))
print(tabla.insertar([6, 'No se debe agregar']))
tabla.insertar(['hola', 'Welmann6'])
tabla.insertar([8, 'Welmann7'])
tabla.insertar([9, 'Welmann8'])
tabla.insertar([10, 'Welmann9'])
tabla.insertar([11, 'Welmann10'])
tabla.insertar([12, 'Welmann21'])
tabla.insertar([13, 'Welmann41'])
tabla.insertar([14, 'Welmann51'])
tabla.insertar([15, 'Welmann61'])
tabla.insertar([16, 'Welmann71'])
tabla.insertar([17, 'Welmann81'])
tabla.insertar([18, 'Welmann91'])
tabla.insertar([100, 'Welmann91'])
tabla.insertar([55, 'Welmann91'])
tabla.insertar([50, 'Welmann9'])
tabla.insertar([51, 'Welmann10'])
tabla.insertar([52, 'Welmann21'])
tabla.insertar([53, 'Primer53'])
tabla.insertar([54, 'Welmann51'])
tabla.insertar([95, 'Welmann61'])
tabla.insertar([56, 'Welmann71'])
tabla.insertar([57, 'Welmann81'])
tabla.insertar([58, 'Welmann91'])
tabla.insertar([120, 'Welmann91'])
tabla.insertar([65, 'Welmann91'])
tabla.insertar([16, 'Welmann71 no se debe insertar'])
tabla.insertar([1, 'Welmann'])
tabla.insertar([53342, 'unico 53342'])
tabla.insertar([12343, 'Welmann41'])
tabla.insertar([14324, 'Welmann51'])
tabla.insertar([143245, 'Welmann61'])
tabla.insertar([13246, 'Welmann71'])
tabla.insertar([14327, 'Welmann81'])
tabla.insertar([13238, 'Welmann91'])
tabla.insertar([10430, 'Welmann91'])
tabla.insertar([5345, 'Welmann91'])
tabla.insertar([53430, 'Welmann9'])
tabla.insertar([5334, 'Welmann41'])
tabla.insertar([1243, 'Welmann41'])
tabla.insertar([4324, 'Welmann51'])
tabla.insertar([14324, 'Welmann61'])
tabla.insertar([1346, 'Welmann71'])
tabla.insertar([1432, 'Welmann81'])
tabla.insertar([138, 'Welmann91'])
tabla.insertar([1043, 'Welmann91'])
tabla.insertar([545, 'Welmann91'])
tabla.insertar([530, 'Welmann9'])
tabla.insertar([53342, 'repetido'])
tabla.insertar([3, 'Welmann2'])



print(tabla.extractTable())

tabla.imprimir()
print('')
tabla2.imprimir()
print()
print()

pruebaBusqueda = [65, 17, 8, 4, 121, 2000, 896]
BusquedaASCII = ['aa', 'aba', 'arr', 'hola', 'puto', 50, 1]

print('BUSQUEDA EN TABLA ENTEROS')
for i in pruebaBusqueda:
    print('Resultado de buscar la llave:', i)
    print(tabla.ExtraerTupla(i))

print()
print('BUSQUEDA EN TABLA STRING')
for i in BusquedaASCII:
    print('Resultado de buscar la llave:', i)
    print(tabla2.ExtraerTupla(i))

print()
print(tabla.ExtraerTupla(52))
tabla.deleteTable(52)
print(tabla.ExtraerTupla(52))

print()
print(tabla.ExtraerTupla(11))
print(tabla.update(11, 1, 'NuevoValor'))
print(tabla.ExtraerTupla(11))

print()
print(tabla2.ExtraerTupla('aa'))
print(tabla2.update('aa', 1, 'Nuevo valor en tabla string'))
print(tabla2.ExtraerTupla('aa'))

print()
print(tabla2.ExtraerTupla('aa'))
tabla2.deleteTable('aa')
print(tabla2.ExtraerTupla('aa'))

tabla.truncate()
tabla.imprimir()
tabla.insertar([4, 'Holuuuuu'])
tabla.imprimir()
tabla.deleteTable(4)
tabla.imprimir()

print(tabla.extractTable())
print(type(45))

tablaAleaoria = Tabla('Aleatoria', 3)

for i in range(200):
    tablaAleaoria.insertar([random.randint(1, 10000), random.randint(1, 100000), random.randint(1,10000)])

print(tablaAleaoria.tamano)
#tablaAleaoria.Grafico()
