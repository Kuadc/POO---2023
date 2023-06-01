import numpy as np

import csv

from ClaseTaller import Taller

from ClaseInscripcion import Inscripcion


class ArregloTaller:

    def __init__(self,dimension,incremento=5):
        self.__arreglo = np.empty(dimension, dtype=Taller)
        self.__dimension = dimension
        self.__incremento = incremento
        self.__cantidad = 0

    def guardainscripcion(self,taller):
        if self.__cantidad == self.__dimension:
            self.__dimension+= self.__incremento
            self.__arreglo.resize(self.__dimension)
        self.__arreglo[self.__cantidad] = taller
        self.__cantidad+=1

    def abrirarchivo(self):
        archivo = open("talleres.csv")
        reader = csv.reader(archivo,delimiter=";")
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                idtaller = int(fila[0])
                nombre = fila[1]
                vacantes = int(fila[2])
                monto = int(fila[3])
                untaller = Taller(idtaller,nombre,vacantes,monto)
                self.guardainscripcion(untaller)
        archivo.close()

    def inscribirpersona(self,persona,fecha,arregloinsc):
        self.mostrardatos()
        codtaller= int(input("Elija el codigo del taller a inscribirse: "))
        pago = False
        if self.__arreglo[codtaller-101].Getvacantes() == 0:
            print("No hay vancantes para el taller elejido")
        else:
            unainscripcion = Inscripcion(fecha,pago,persona,self.__arreglo[codtaller-101])
            arregloinsc.guardainscripcion(unainscripcion)
            self.__arreglo[codtaller-101].nuevainscripcion(unainscripcion)
            self.__arreglo[codtaller-101].modificarvacante()

    def mostrardatos(self):
        for i in range(self.__cantidad):
            print(self.__arreglo[i])
        return

    def buscarincriptos(self):
        codtaller = int(input("Ingrese el codigo del taller: "))
        i = 0
        bandera = False
        while i<self.__cantidad and not bandera:
            taller = self.__arreglo[i]
            if codtaller == taller.Getcodtaller():
                taller.mostrarpersonas()
                bandera = True
            else:
                i= i+1
