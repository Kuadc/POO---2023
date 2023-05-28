import json

from ClaseVehiculo import Vehiculo

from ClaseVehiculoNuevo import VehiculoNuevo

class Nodo:
    __vehiculo=None
    __siguiente=None

    def __init__(self, electro):
        self.__vehiculo=electro
        self.__siguiente=None

    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente

    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__vehiculo

    def toJSON(self):
        d = dict(
        __class__=self.__class__.__name__,
        __atributos__=dict(
        vehiculo = self.__vehiculo.toJSON()
        ))
        return d
