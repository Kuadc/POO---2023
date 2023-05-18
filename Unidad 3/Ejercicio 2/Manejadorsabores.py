import csv

import numpy as np

from clasesabores import sabores

class listasabores:
    __listasabor = []

    def __init__(self):
        self.__listasabor = []


    def abrirarchivo(self):
        archivo = open("sabores.csv")
        reader = csv.reader(archivo, delimiter = ",")
        for fila in reader:
            unsabor = sabores(int(fila[0]),fila[1],fila[2])
            self.__listasabor.append(unsabor)
        archivo.close()

    def __str__(self):
        s= ""
        for sabor in self.__listasabor:
            s+= str(sabor) +"\n"
        return s


    
    def mostrarsabores(self,indices):
        i=0
        while i<len(indices):
            print(self.__listasabor[indices[i]])
            i=i+1
            
    def buscarsabor(self,indice):
        return self.__listasabor[indice]
    
    def mostrarsabor(self,indice):
        print("Sabor")
        print(self.__listasabor[indice-1])