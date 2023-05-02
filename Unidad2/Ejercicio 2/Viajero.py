
'''
Clase:
    ViajeroFrecuente:
    Atributos(int,int,string,string,int)
Funciones:
    Constructor(int,string,string,string,int)
    __str__(imprime el objeto)
'''


class viajeroFrecuente:
    __numviajero = 0
    __dni = 0
    __nombre = ""
    __apellido = ""
    __millas_acum = 0
    
    def __init__(self, numviajero=0,dni=0,nombre="",apellido="",millas=0):
        self.__numviajero = numviajero
        self.__dni = dni
        self.__nombre = nombre
        self.__millas_acum = millas
        
    def cantidadTotaldeMillas(self):
        return self.__millas_acum
    
    def acumularMillas(self,millas):
        self.__millas_acum+=millas
        return self.__millas_acum
    
    def canjearMillas(self,millas):
        if millas > self.__millas_acum:
            print("No tiene suficientes millas para canjear")
        else:
            self.__millas_acum = self.__millas_acum - millas
        return self.__millas_acum
            
    def Getnumviajero(self):
        return self.__numviajero