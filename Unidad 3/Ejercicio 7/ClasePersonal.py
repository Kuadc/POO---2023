
class Personal():
    __cuil = ""
    __apellido = ""
    __nombre = ""
    __sueldobasico = 0.0
    __antiguedad = 0

    def __init__(self,**kwargs):
        self.__cuil = kwargs['cuil']
        self.__apellido = kwargs['apellido']
        self.__nombre = kwargs['nombre']
        self.__sueldobasico = int(kwargs['sueldobasico'])
        self.__antiguedad = int(kwargs['antiguedad'])

    def __str__(self):
        cadena = ""
        cadena+= "\nTipo de personal: {} \ncuil: {} \napellido: {} \nnombre: {} \nsueldo basico: {} \nantiguedad: {}".format(type(self).__name__,self.__cuil,self.__apellido,self.__nombre,self.__sueldobasico,self.__antiguedad)
        return cadena

    def getApellido(self):
        return self.__apellido

    def getcuil(self):
        return self.__cuil

    def getnombre(self):
        return self.__nombre

    def getsueldobasico(self):
        return self.__sueldobasico

    def getantiguedad(self):
        return self.__antiguedad

    def mostrarsueldo(self):
        pass

    def mostrardatos(self):
        print("Nombre:{} Apellido: {}".format(self.__nombre,self.__apellido))
