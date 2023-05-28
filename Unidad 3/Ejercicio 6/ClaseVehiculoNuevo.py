
from ClaseVehiculo import Vehiculo

class VehiculoNuevo(Vehiculo):
    __marca = ""
    __version = ""
    def __init__(self, modelo, puertas, color, preciobase, marca, version):
        super().__init__(modelo, puertas, color, preciobase)
        self.__marca = marca
        self.__version = version

    def getmarca(self):
        return self.__marca

    def getversion(self):
        return self.__version
    def getpreciobase(self):
        return Vehiculo.getpreciobase(self)

    def __str__(self):
        return "Modelo:%s Puertas: %s Color: %s Precio Base: %s Marca:%s Version:%s "%(self.getmodelo(),self.getpuertas(),self.getcolor(),self.getpreciobase(),self.__marca,self.__version)
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__=dict(
                modelo = self.getmodelo(),
                puertas = self.getpuertas(),
                color = self.getcolor(),
                preciobase = self.getpreciobase(),
                marca = self.__marca,
                version = self.__version
            )
        )
        return d
