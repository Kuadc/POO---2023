
import json

from ClaseNodo import Nodo

from zope.interface import implementer

from ClaseInterfaz import EjercicioInterface

from ClaseVehiculoUsado import VehiculoUsado

from ClaseVehiculoNuevo import VehiculoNuevo

@implementer(EjercicioInterface)
class Lista:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None


    def AgregarElemento(self, unelectro):
        #if isinstance(unelectro,object):
        nodo = Nodo(unelectro)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual=nodo
        self.__tope+=1
        #else:
            #raise AttributeError

    def InsertarElemento(self,elemento,pos):
        if pos == 0:
            self.AgregarElemento(elemento)
        else:
            i=0
            aux = self.__comienzo
            anterior = self.__comienzo
            while i<pos and aux != None: # inicializamos i en 0 para recorrer la lista de nodos
                anterior = aux
                aux = aux.getSiguiente()
                i+=1
            if pos == i:
                nodo = Nodo(elemento)
                anterior = nodo.getSiguiente()
                nodo.setSiguiente(aux)
                self.__tope+=1
            else:
                raise IndexError

    def getTope(self):
        return self.__tope

    def MostrarElemento(self,pos):
        if isinstance(pos,int):
            i=0
            aux = self.__comienzo
            while i<pos and aux != None:
                aux = aux.getSiguiente()
                i+=1
            if pos == i:
                print(aux.getDato().__class__.__name__)
                return aux.getDato().__class__
            else:
                raise IndexError

    def BuscarMarca(self,patente):
        if isinstance(patente,str):
            encontrado = False
            aux = self.__comienzo
            while not encontrado and aux != None:
                if isinstance(aux.getDato(),VehiculoUsado):
                    if aux.getDato().getpatente() == patente:
                        encontrado = True
                        precio =int(input("Ingrese el nuevo precio de venta"))
                        aux.getDato().cambiarpreciosbase(precio)
                        aux.getDato().importeventa()
                        return aux.getDato()
                    else:
                        aux = aux.getSiguiente()
                else:
                    aux = aux.getSiguiente()
        else:
            print("el parametro recibido no es correcto")

    def buscareconomico(self):
        aux = self.__comienzo
        min = 999999
        while aux != None:
            precio = aux.getDato().getpreciobase()
            if precio < min:
                min = precio
                vehiculo = aux.getDato()
                aux = aux.getSiguiente()
            else:
                aux = aux.getSiguiente()

        print("El Vehiculo mas economico es el siguiente")
        print(vehiculo)
        vehiculo.importeventa()

    def toJSON(self):
            d = dict(
            __class__ = self.__class__.__name__,
            Vehiculo = [Nodo.toJSON() for Nodo in self] 
            )
            return d

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato


