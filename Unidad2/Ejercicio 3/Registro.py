

class registro:
    __temperatura = 0
    __humedad = 0
    __presion = 0
    
    def __init__(self, temperatura=0,humedad=0,presion=0):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion = presion
    
    def Gettemp(self):
        return self.__temperatura
    
    def Gethumedad(self):
        return self.__humedad
    
    def Getpresion(self):
        return self.__presion
    
    def __str__(self):
        return "%s %s %s"%(self.__temperatura,self.__humedad,self.__presion)
        
    