import csv

from Clasehelado import helado

from clasesabores import sabores

class listahelado:
    __listahelado = []

    def __init__(self):
        self.__listahelado= []

    def venderhelado(self,listasab):
        cantidad = int(input("ingrese cantidad de sabores"))
        arreglocodigos = listasab.elejirsabor()
        unhelado = helado()
        self.__listahelado = listasab.cargasabor(arreglocodigos)





