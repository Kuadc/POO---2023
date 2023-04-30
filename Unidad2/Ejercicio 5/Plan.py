
class PlanAhorro:
    cantidadcuotasplan = 60
    cantidadcuotaslicitar = 30 
    
    def __init__(self, codigo=0,modelo="",version="",valorvehiculo=0):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version = version
        self.__valorvehiculo = valorvehiculo
        
    @classmethod
    def getcantcuotas (cls):
        return cls.cantidadcuotasplan
    
    @classmethod
    def getcantcuotaslicitar(cls):
        return cls.cantidadcuotaslicitar
    
    @classmethod
    def vercuotas(cls):
        print("variables de clase")
        print("cantidad de cuotas: %s" %(PlanAhorro.getcantcuotas()))
        print("cantidad de cuotas a licitar: "+str(cls.cantidadcuotaslicitar))
        
    def ModificarValorVehiculo(self,valor):
        self.__valorvehiculo = valor
        return
    
    def mostrarDatos(self):
        print("codigo: %s   - Modelo: %s    - Version: %s" %(self.__codigo,self.__modelo,self.__version))
    
    def GetValor(self):
        return self.__valorvehiculo
    def __str__(self):
        return "Codigo: %s , modelo: %s , version: %s, valorvehiculo: %s" %(self.__codigo, self.__modelo, self.__version, self.__valorvehiculo)
    
    @classmethod
    def Cambiarvariables(cls):
        cls.cantidadcuotaslicitar = 15
        cls.cantidadcuotasplan = 84