import csv

import numpy as np

from ClaseInscripcion import Inscripcion


class ListaInscripcion:

    def __init__(self,dimension,incremento):
        self.__arreglo = np.empty(dimension, dtype= Inscripcion)
        self.__dimension = dimension
        self.__incremento = incremento
        self.__cantidad = 0

    def guardainscripcion(self,inscripcion):
        if self.__cantidad == self.__dimension:
            self.__dimension+= self.__incremento
            self.__arreglo.resize(self.__dimension)
        self.__arreglo[self.__cantidad] = inscripcion
        self.__cantidad+=1

    def cambiarestadodni(self,dni):
        i=0
        bandera = False
        while not bandera and i<self.__cantidad:
            print("dentro del while")
            persona = self.__arreglo[i].Getpersona()
            if dni == persona.getdni():
                self.__arreglo[i].Cambiarpago()
                bandera = True
            else:
                i= i+1
        if bandera == False:
            print("Dni no encontrado")
        else:
            print("Persona encontrada, pago realizado")

    def buscardni(self,dni):
        i=0
        bandera = False
        while i<self.__cantidad:
            persona = self.__arreglo[i].Getpersona()
            if dni == persona.getdni():
                self.__arreglo[i].Gettaller().mostrartaller()
                if self.__arreglo[i].Getpago() == False:
                    print("El mondo adeudado es de :{}".format(self.__arreglo[i].Gettaller().getmontoinscripcion()))
                    i=i+1
                else:
                    print("La persona no Adeuda inscripcion")
                    i=i+1
            else:
                i=i+1

    def guardarenarchivo(self):
        lista =[]
        for i in range(self.__cantidad):
            lista2 = [self.__arreglo[i].Getpersona().getdni(),self.__arreglo[i].Gettaller().Getcodtaller(),self.__arreglo[i].getfecha(),self.__arreglo[i].Getpago()]
            lista.append(lista2)
            lista2 = []
        np.savetxt("Inscripciones.csv", lista, delimiter =",",fmt ='% s')
        return
        






