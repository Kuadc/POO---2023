from ClaseEmpleado import Empleado

'''Sueldo = sueldo básico+ 1% del sueldo básico*antigüedad'''


class EmpleadoPlanta(Empleado):
    __sueldobasico = 0
    __antiguedad = 0

    def __init__(self, **kwargs):
        Empleado.__init__(self,**kwargs)
        self.__sueldobasico = kwargs['sueldobasico']
        self.__antiguedad = kwargs['antiguedad']

    def __str__(self):
        cadena = ' ______Empleado de Planta_________\n '
        cadena+= 'Empleado de Planta - DNI: {} \n Nombre:{} \n Direccion: {} \n Telefono: {} \n Sueldo Basico:{} \n antiguedad:{}'.format(self.getdni(),self.getnombre(),self.getdireccion(),
                                                                                                                                          self.gettelefono(),self.__sueldobasico,self.__antiguedad)
        return cadena

    def calcularsueldo(self):
        antiguedad = (self.__sueldobasico*self.__antiguedad)*0.01
        sueldo = self.__sueldobasico+antiguedad
        return sueldo

    def mostrarnomytel(self):
        print("______Empleado/s Planta Permanente______")
        Empleado.mostrarnomytel(self)