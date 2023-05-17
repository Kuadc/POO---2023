
class Carrera():
    __codigo = 0
    __nombre = ""
    __titulo = 0
    __duracion = ""
    __grado = ""

    def __init__(self,codigo,nombre,titulo,duracion,grado):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__Titulo = titulo
        self.__duracion = duracion
        self.__grado = grado

    def __str__(self):
        return "%s %s %s %s %s" % (self.__codigo,self.__nombre,self.__duracion,self.__Titulo,self.__grado)

    def Getnomcarrera(self):
        return self.__nombre

    
    def Getcodcarrera(self):
        return "%s" % (self.__codigo)

    def mostrarnombreyduracion(self):
        return "Nombre Carrera:%s       Duracion: %s" % (self.__nombre,self.__duracion)
