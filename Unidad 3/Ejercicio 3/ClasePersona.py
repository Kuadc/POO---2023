
class Persona:
    __nombre = ""
    __direccion = ""
    __dni = ""

    def __init__(self, nombre, direccion, dni):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__dni = dni

    def getdni(self):
        return self.__dni

    def __str__(self):
        return "nombre:%s direccion:%s dni:%s"%(self.__nombre,self.__direccion,self.__dni)


