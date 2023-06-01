

class Inscripcion:
    __fecha = ""
    __pago = False
    __persona = object
    __taller = object

    def __init__(self, fecha, pago, persona,taller):
        self.__fecha = fecha
        self.__pago = pago
        self.__persona = persona
        self.__taller = taller

    def Getpersona(self):
        return self.__persona

    def Getpago(self):
        return self.__pago

    def Cambiarpago(self):
        self.__pago = True

    def Gettaller(self):
        return self.__taller

    def getfecha(self):
        return self.__fecha

    def Cambiarpersona(self):
        self.__persona.cambiarpago()
