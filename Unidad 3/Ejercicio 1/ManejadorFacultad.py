import csv

from ClaseCarrera import Carrera

from ClaseFacultad import Facultad


class ListaFacultad:
    __lista = []
    
    def __init__(self):
        self.__lista = []
        
    def AbrirArchivo(self):
        archivo = open("facultad.csv",encoding = "utf-8")
        reader = csv.reader(archivo,delimiter = ",")
        codigobandera = next(reader)
        Bandera = True
        listacarrera = []
        while Bandera:
            codcarrre = next(reader)
            listacarrera.clear()
            while Bandera and (codigobandera[0] == codcarrre[0]):
                listacarrera.append(codcarrre)
                try:
                    codcarrre = next(reader)
                except StopIteration:
                    Bandera = False
            codigo = int(codigobandera[0])
            nombre = codigobandera[1]
            direccion = codigobandera[2]
            localidad = codigobandera[3] 
            telefono = codigobandera[4]
            unafacultad = Facultad(codigo, nombre, direccion, localidad, telefono,listacarrera)
            self.__lista.append(unafacultad)
            codigobandera = codcarrre
        archivo.close()
    
    
    def mostrarfacultad(self, cod):
        i=0
        bandera = True
        while bandera and i<len(self.__lista):
            if cod == self.__lista[i].GetcodigoFacu():
                print("\nNombre de la Facutad: %s \n" %( self.__lista[i].Getnombre()))
                self.__lista[i].mostrarcarreras()
                bandera = False
            else:
                i=i+1
        return 
    
    def mostrarcodigo(self, nombre):
        i=0
        j=0
        bandera = True
        while bandera and i<len(self.__lista):
            listacarrera = self.__lista[i].Getcarrera()
            while bandera and j<len(listacarrera):                
                if nombre == listacarrera[j].Getnomcarrera():
                    print("\nCodigo de la carrera: %s.%s"%(i+1,listacarrera[j].Getcodcarrera()))
                    print("Nombre de la Facutad: %s " %( self.__lista[i].Getnombre()))
                    print("Localidad: %s" %(self.__lista[i].Getlocalidad()))
                    bandera = False
                else: j=j+1
            i=i+1
            j=0
        return
        
        
    def __str__(self):
        s= ""
        for facultad in self.__lista:
            s += str(facultad) +"\n"
        return s
        
        