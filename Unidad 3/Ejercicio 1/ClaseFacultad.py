from ClaseCarrera import Carrera


class Facultad():
    __codigo = 0
    __nombre = ""
    __direccion = ""
    __localitad = ""
    __telefono= ""
    __carrera = []

    def __init__(self,codigo,nombre,direccion,localidad,telefono,listacarrera):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localitad = localidad
        self.__telefono = telefono
        self.__carrera = []
        for fila in listacarrera:
            unacarrera = Carrera(int(fila[1]), fila[2], fila[3], fila[4], fila[5])
            self.__carrera.append(unacarrera)

    def __str__(self):
        s = ""
        s+= "%s %s %s %s %s\n\n" % (self.__codigo,self.__nombre,self.__direccion,self.__localitad,self.__telefono)
        for i in range(len(self.__carrera)):
            s+= str(self.__carrera[i]) +"\n"
        return s

    def Getcarrera(self):
        return self.__carrera
    def GetcodigoFacu(self):
        return self.__codigo
    
    def Getlocalidad(self):
        return self.__localitad
    def Getnombre(self):
        return self.__nombre
    
    def mostrarcarreras(self):
        for i in range(len(self.__carrera)):
            print(self.__carrera[i])
        return 
