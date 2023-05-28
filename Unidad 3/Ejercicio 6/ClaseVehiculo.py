import json

class Vehiculo:
    __modelo = ""
    __puertas = ""
    __color = ""
    __preciobase = 0
    def __init__(self, modelo, puertas, color, preciobase):
        self.__modelo = modelo
        self.__puertas = puertas
        self.__color = color
        self.__preciobase = int(preciobase)

    def getmodelo(self):
        return self.__modelo

    def getpuertas(self):
        return self.__puertas

    def getcolor(self):
        return self.__color

    def getpreciobase(self):
        return self.__preciobase

    def cambiarpreciosbase(self,precio):
        self.preciobase = precio
    def toJSON(self):
        pass




