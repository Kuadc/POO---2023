
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
                print(aux.getDato())
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
                        aux.getDato().cambiarpreciosbnase(precio)
                        vehiculo = aux.getDato()
                        self.importeventa(vehiculo)
                    else:
                        aux = aux.getSiguiente()
                else:
                    aux = aux.getSiguiente()
        else:
            print("el parametro recibido no es correcto")

    def importeventa(self,vehiculo):
        if isinstance(vehiculo,VehiculoUsado):
            precio = vehiculo.getpreciobase()
            año = 2023 - vehiculo.getanio()
            antiguedad = (precio * año) / 100
            if vehiculo.getkilometraje() > 100000:
                preciokm = (precio * 2) / 100
                gastos = (precio * 0.10)
                preciobase = (antiguedad + preciokm + gastos) - precio
                print("el precio de venta es de: ", preciobase)
            else:
                gastos = (precio * 0.10)
                preciobase = (precio +gastos)- antiguedad
                print("el precio de venta es de: ", preciobase)
        else:
            precio = vehiculo.getpreciobase()
            if vehiculo.getversion() == "full":
                full = (precio *0.02)
                preciobase = ((precio * 0.1)+precio)+full
                print("el precio de venta es de: ", preciobase)
            else:
                preciobase = (precio *0.10)+precio
                print("El precio de venta es de: ", preciobase)

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
        self.importeventa(vehiculo)

    def toJSON(self):
            d = dict(
            __class__ = self.__class__.__name__,
            Vehiculo = [Nodo.toJSON() for Nodo in self] #como la lista se puede iterar gracias a los metodos "next" e "iter" podemos recorrer la lista de esta manera, con lo cual por cada nodo es la lista, llama al nodo.toJSON. que segun el nodo que tenga guardado, puede ser una instancia de la clase vehiculousado o vehiculonuevo. por lo tanto llamaria a vehiculousado.toJSON
            )
            return d
    # necesito que for nodo in "self". ya que necesito el objeto lista entero(comienzo,actual,indice,tope) para que sea iterable. no puedo hacer self.comienzo

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


