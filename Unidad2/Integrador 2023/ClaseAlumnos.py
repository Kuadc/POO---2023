# La estructura del mismo es la siguiente: dni, apellido, nombre, carrera, año de la carrera que cursa.


class Alumnos:
    __dni = ""
    __apellido = ""
    __nombre = ""
    __carrera = ""
    __año = ""

    def __init__(self, dni="", apellido="", nombre="", carrera="", año=""):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__año = año


    def __str__(self):
        return 'DNI= %s \n apellido= %s \n nombre = %s \n carrera = %s \n año = %s\n' % (self.__dni, self.__apellido, self.__nombre, self.__carrera, self.__año)
    
    def __gt__(self, other):
        if type(other) == str:
            return self.__apellido > other
        else:
            return self.__año > other
        
    def Getdni(self):
        return self.__dni

    def Getaño(self):
        return self.__año

    def Getnombreyapellido(self):
        s = ""
        s+= str(self.__apellido)+","+str(self.__nombre)
        return s

    def Getapellido(self):
        return self.__apellido
