
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
        self.__apellido = apellido
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
    
    def __gt__(self,viajero):
        band = False
        if self.__millas_acum > viajero.cantidadTotaldeMillas():
            band = True
        return band
    
    def __add__(self,millas):
        millastotoales= self.__millas_acum + millas
        viajero = viajeroFrecuente(self.__numviajero,self.__dni,self.__nombre,self.__apellido,millastotoales)
        return viajero
    
    def __sub__(self,millas):
        millastotoales= self.__millas_acum - millas
        viajero = viajeroFrecuente(self.__numviajero,self.__dni,self.__nombre,self.__apellido,millastotoales)
        return viajero
        
            
    
    def __str__(self):
        return "Numero de viajero: %s \n DNI: %s \n Nombre y apellido: %s  %s \n Millas acumuladas: %s" %(self.__numviajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum)