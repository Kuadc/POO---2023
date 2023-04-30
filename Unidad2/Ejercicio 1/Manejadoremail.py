import csv
from email import email

class Manejadorviajero:
    __listamail = []
    def __init__(self):
        self.__listamail = []

    def agregaremail(self,unmail):
        self.__listamail.append(unmail)

    def buscardominio(self, clave):
        return

    def __str__(self):
        s = ""
        for libro in self.__listaLibros:
            s += str(libro) + '\n'
        return s

    def abrirArchivo(self):
        archivo = open('listaviajero.csv')
        lista = csv.reader(archivo,delimiter=',')
        bandera = True
        for fila in lista:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
                print(fila)
                bandera2= self.verificadorcorreo(fila)
                if bandera2 == True:
                    unmail = email(fila[0],fila[1],fila[2],fila[3])
                    self.agregaremail(unmail)
        archivo.close()

    def verificadorcorreo(self,fila):
        bandera = True
        if fila[0] == "" or fila[1] == "" or fila[2] == "" :
            bandera = False
            print("Correo erroneo: {}{}{}" .format(fila[0],fila[1],fila[2]))
        return bandera

