"""La estructura de dicho archivo es la siguiente: dni, nombre de materia, fecha, nota,
aprobación (‘E’ – Examen, ‘X’ – Equivalencia, ‘P’ – Promoción)."""


class Materia:
    __dni = ""
    __materia = ""
    __fecha = ""
    __nota = 0
    __aprovacion = ""

    def __init__(self, d="", m="", f="", n=0, aprov=""):
        self.__dni = d
        self.__materia = m
        self.__fecha = f
        self.__nota = n
        self.__aprovacion = aprov

    def __str__(self):
        return "DNI= %s \n Materia= %s \n Fecha = %s \n Nota = %s \n Aprobacion = %s\n" %(self.__dni,self.__materia,self.__fecha,self.__nota,self.__aprovacion)

    def Getmateria(self):
        return self.__materia

    def Getdni(self):
        return self.__dni

    def Getnota(self):
        return self.__nota

    def Getfecha(self):
        return self.__fecha

    def Getaprovacion(self):
        return self.__aprovacion
