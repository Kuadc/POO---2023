import csv

from ClaseMaterias import Materia

class ListaMateria:
    __lista = []

    def __int__(self):
        self.__lista = []

    def AbrirArchivo(self):
        archivo = open("materiasAprobadas.csv")
        reader = csv.reader(archivo,delimiter=";")
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                dni = fila[0]
                materia = fila[1]
                fecha = fila[2]
                nota = int(fila[3])
                aprovacion = fila[4]
                unamateria = Materia(dni, materia, fecha, nota,aprovacion)
                self.__lista.append(unamateria)
        archivo.close()

    def BuscarAlumno(self, dni):
        i = 0
        aplazo = 0
        sinaplazo = 0
        contadoraplazo = 0
        contadorsinaplazo = 0
        while i < len(self.__lista):
            if dni == self.__lista[i].Getdni():
                nota = self.__lista[i].Getnota()
                print("Materia: {} nota: {}".format(self.__lista[i].Getmateria(),nota))
                if nota < 5:
                    aplazo += nota
                    contadoraplazo += 1
                    i = i + 1
                else:
                    sinaplazo+=nota
                    contadorsinaplazo+=1
                    i = i + 1
            else:
                i= i+1
        aplazo = (aplazo+sinaplazo)/(contadoraplazo+contadorsinaplazo)
        print("El promedio con aplazos es de : {}" .format(aplazo))
        sinaplazo = sinaplazo/contadorsinaplazo
        print("El promedio con sin aplazos es de : %s" % (sinaplazo))

    def BuscarMateria(self,arreglo,materia):
        i = 0
        while i < len(self.__lista):
            notas = self.__lista[i].Getnota()
            if materia == self.__lista[i].Getmateria() and "P" == self.__lista[i].Getaprovacion() and notas >= 7:
                """DNI - Apellido y nombre - Fecha - Nota - Año que cursa"""
                x= 'Dni'
                a= "Apellido y Nombre"
                f= "Fecha"
                n= "Nota"
                año = "Año que cursa"
                print("{:^15}{:^15}{:^15}{:^15}{:^15}".format(x,a,f,n,año))
                dni = self.__lista[i].Getdni()
                fecha = self.__lista[i].Getfecha()
                nota = self.__lista[i].Getnota()
                nya = arreglo.BuscarNyA(self.__lista[i].Getdni())
                añocursa = arreglo.BuscarAño(self.__lista[i].Getdni())
                print("{:^15}{:^15}{:^15}{:^15}{:^15}".format(dni,nya,fecha,nota,añocursa))
                i = i+1
            else:
                i = i+1
        return

    def __str__(self):
        s = ""
        for materia in self.__lista:
            s+= str(materia) + "\n"
        return s
