from ClaseVehiculo import Vehiculo
class VehiculoUsado(Vehiculo):
    __marca = ""
    __patente = ""
    __anio = 0
    __kilometraje = 0
    def __init__(self, modelo, puertas, color, preciobase, marca, patente, anio, kilometraje):
        super().__init__(modelo, puertas, color, preciobase)
        self.__marca = marca
        self.__patente = patente
        self.__anio = anio
        self.__kilometraje = kilometraje

    def getmarca(self):
        return self.__marca

    def getpatente(self):
        return self.__patente

    def getanio(self):
        return self.__anio

    def getkilometraje(self):
        return self.__kilometraje

    def cambiarpreciosbnase(self,precio):
        Vehiculo.cambiarpreciosbase(self,precio)

    def getpreciobase(self):
        return Vehiculo.getpreciobase(self)

    def __str__(self):
        return "Modelo:%s Puertas: %s Color: %s Precio Base: %s Marca:%s Patente:%s Año:%s Kilometraje: %s"%(self.getmodelo(),self.getpuertas(),self.getcolor(),self.getpreciobase(),self.__marca,self.__patente,self.__anio,self.__kilometraje)

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__=dict(
                modelo = self.getmodelo(),
                puertas = self.getpuertas(),
                color = self.getcolor(),
                preciobase = self.getpreciobase(),
                marca = self.__marca,
                patente = self.__patente,
                anio = self.__anio,
                kilometraje = self.__kilometraje
            )
        )
        return d