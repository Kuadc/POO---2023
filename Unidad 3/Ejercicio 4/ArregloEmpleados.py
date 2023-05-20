import csv

import datetime

import numpy as np

from ClaseEmpleado import Empleado

from ClaseEmpleadoPLanta import EmpleadoPlanta

from ClaseEmpleadoContratado import EmpleadoContratado

from ClaseEmpleadoExterno import EmpleadoExterno


class Arreglo:

    def __init__(self,dimension,incremento=5):
        self.__arreglo = np.empty(dimension, dtype=Empleado)
        self.__dimension = dimension
        self.__incremento = incremento
        self.__cantidad = 0

    def agregarempleado(self,empleado):
        if self.__cantidad == self.__dimension:
            self.__dimension+= self.__incremento
            self.__arreglo.resize(self.__dimension)
        self.__arreglo[self.__cantidad] = empleado
        self.__cantidad+=1

    def abrirplanta(self):
        archivo = open('planta.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            dn = fila[0]
            nom = fila[1]
            dire = fila[2]
            tele = fila[3]
            basico = int(fila[4])
            anti = int(fila[5])
            empleado = EmpleadoPlanta(dni= dn,nombre=nom,direccion=dire,telefono=tele,sueldobasico=basico,antiguedad=anti)
            self.agregarempleado(empleado)
        archivo.close()

    def abrircontratado(self):
        archivo = open('contratado.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            dn = fila[0]
            nom = fila[1]
            dire = fila[2]
            tele = fila[3]
            fechaini = fila[4]
            fechafin = datetime.datetime.strptime(fila[5], "%Y/%m/%d").date()
            hor = int(fila[6])
            vhora = int(fila[7])
            empleado = EmpleadoContratado(dni=dn, nombre=nom, direccion=dire, telefono=tele, fechainicio=fechaini,fechafinalizacion=fechafin,
                                      horas=hor,valorhora=vhora)
            self.agregarempleado(empleado)
        archivo.close()

    def abrirexterno(self):
        archivo = open('externo.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            dn = fila[0]
            nom = fila[1]
            dire = fila[2]
            tele = fila[3]
            tar = fila[4]
            fechaini = fila[5]
            fechafin = datetime.datetime.strptime(fila[6], "%Y/%m/%d").date()
            viat = int(fila[7])
            cos = int(fila[8])
            mon = int(fila[9])
            empleado = EmpleadoExterno(dni= dn,nombre=nom,direccion=dire,telefono=tele,
                                       tarea=tar,fechainicio=fechaini,fechafinalizacion=fechafin,viatico=viat,costo=cos,montoseguro=mon)
            self.agregarempleado(empleado)
        archivo.close()

    def mostrardatos(self):
        for i in range(self.__cantidad):
            empleado = self.__arreglo[i]
            print(empleado)

    def Buscareincrementar(self,dni,horas):
        i = 0
        bandera = True
        while bandera and i<self.__cantidad:
            empleado = self.__arreglo[i]
            if isinstance(empleado,EmpleadoContratado):
                if dni == empleado.getdni():
                    print("Horas trabajadas: {}".format(empleado.gethoras()))
                    empleado.cambiarhoras(horas)
                    print("Nuevo total de horas trabajadas: {}".format(empleado.gethoras()))
                    bandera = False
                else:
                    i=i+1
            else:
                i=i+1
        if bandera == True:
            print("Empleado no encontrado")

    def buscartarea(self,tarea):
        '''Sueldo = costo de la obra - viático- monto del seguro de vida'''
        i = 0
        bandera = True
        while bandera and i < self.__cantidad:
            empleado = self.__arreglo[i]
            if isinstance(empleado,EmpleadoExterno):
                fechaactual = datetime.date.today()
                if  tarea == empleado.gettarea() and empleado.getfechafinalizacion() > fechaactual:
                    sueldo = (empleado.getcosto() - empleado.getviatico())-empleado.getmontoseguro()
                    print(empleado)
                    print("Monto a pagar por la Tarea: ",sueldo)
                    bandera = False
                else:
                    i=i+1
            else:
                i=i+1

    def ayudaeconomica(self):
        """listar nombre, dirección y DNI de los empleados que les corresponde la ayuda."""
        i = 0
        while i < self.__cantidad:
            empleado = self.__arreglo[i]
            if empleado.calcularsueldo() <150000:
                empleado.listarempleado()
                i=i+1
            else:
                i=i+1

    def calcularymostrarsueldo(self):
        i = 0
        while i < self.__cantidad:
            empleado = self.__arreglo[i]
            sueldo = empleado.calcularsueldo()
            self.__arreglo[i].mostrarnomytel()
            print("Sueldo a cobrar:",sueldo)
            i =i+1