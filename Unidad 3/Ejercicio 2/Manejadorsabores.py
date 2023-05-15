import csv

import numpy as np

impot numpy as np
from clasesabores import sabores

class listasabores:
    __listasabor = []

    def __init__(self):
        self.__listasabor = []


    def abrirarchivo(self):
        archivo = open("sabores.csv")
        reader = csv.reader(archivo, delimitter = ",")
        for fila in reader:
            unsabor = sabores(int(fila[0]),fila[1],fila[2])
            self.__listasabor.append(unsabor)
        archivo.close()

    def __mostrarsabores(self):
        for sabor in self.__listasabor:
            sabor.mostrarsabor()


    def elejirsabor(self):
        print("Elija un maximo de cuatro sabores")
        self.__mostrarsabores()
        arreglo = np.empty(4, dtype=int)
        for i in arreglo:
            cod = int(input("Elija codigo de sabor: "))
            arreglo[i] = cod

        return arreglo


