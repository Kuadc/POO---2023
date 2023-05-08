import csv

import numpy as np

from ClaseAlumnos import Alumnos


class ArregloAlumnos:
    __cantidad = 0
    __dimension = 0
    __incremento = 0
    __alumno = None

    def __init__(self, dimension, incremento=5):
        self.__alumno = np.empty(dimension, dtype=Alumnos)
        self.__dimension = dimension
        self.__cantidad = 0
        self.__incremento = incremento

    def AgregarAlumno(self, alu):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__alumno.resize(self.__dimension)
        self.__alumno[self.__cantidad] = alu
        self.__cantidad += 1

    def AbrirArchivo(self):
        archivo = open("alumnos.csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                dni = fila[0]
                apellido = fila[1]
                nombre = fila[2]
                carrera = fila[3]
                año = fila[4]
                unalumno = Alumnos(dni, apellido, nombre, carrera, año)
                self.AgregarAlumno(unalumno)
        archivo.close()

    def Ordenar(self):
        for i in range(1, self.__cantidad):
            aux = self.__alumno[i]
            valor = self.__alumno[i].Getapellido()
            j = i - 1
            while j >= 0 and self.__alumno[j] > valor  : #si utilizamos el operador "<" la lista se ordenaria de mayor a menor.
                self.__alumno[j + 1] = self.__alumno[j]
                j = j - 1
            self.__alumno[j + 1] = aux
        for i in range(1, self.__cantidad):
            aux = self.__alumno[i]
            año = int(self.__alumno[i].Getaño())
            j = i - 1
            while j >= 0 and self.__alumno[j] > año  :
                self.__alumno[j + 1] = self.__alumno[j]
                j = j - 1
            self.__alumno[j + 1] = aux    

    def mostrardatos(self):
        for indice in range(self.__cantidad):
            print(self.__alumno[indice])
        return

    def BuscarNyA(self, dni):
        i = 0
        band = False
        nya = ""
        while i < self.__cantidad and band == False:
            if dni == self.__alumno[i].Getdni():
                nyp = self.__alumno[i].Getnombreyapellido()
                band = True
            else:
                i = i + 1
        return nyp

    def BuscarAño(self, dni):
        i = 0
        band = False
        año = ""
        while i < self.__cantidad and band == False:
            if dni == self.__alumno[i].Getdni():
                año = self.__alumno[i].Getaño()
                band = True
            else:
                i = i + 1
        return año
