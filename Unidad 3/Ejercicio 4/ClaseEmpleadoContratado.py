
from ClaseEmpleado import Empleado
'''Sueldo = cantidad de horas trabajadas * valor de la hora'''


class EmpleadoContratado(Empleado):
    __fechainicio = ""
    __fechafinalizacion = ""
    __horas = ""
    __valorhora = ""

    def __init__(self, **kwargs):
        Empleado.__init__(self,**kwargs)
        self.__fechainicio = kwargs['fechainicio']
        self.__fechafinalizacion = kwargs['fechafinalizacion']
        self.__horas = kwargs['horas']
        self.__valorhora = kwargs['valorhora']

    def __str__(self):
        cadena = ' ______Empleado Contratado_________\n '
        cadena+='DNI: {} \n Nombre:{} \n Direccion: {} \n Telefono: {} '.format(self.getdni(),self.getnombre(),self.getdireccion(),self.gettelefono())
        cadena+='\n Fecha Inicio:{}\n Fecha Finalizacion:{}\n Horas:{}\n Valor Hora:{}'.format(self.__fechainicio,self.__fechafinalizacion,self.__horas,self.__valorhora)
        return cadena

    def cambiarhoras(self,horas):
        self.__horas+= horas

    def gethoras(self):
        return self.__horas

    def calcularsueldo(self):
        sueldo = self.__horas*self.__valorhora
        return sueldo

    def mostrarnomytel(self):
        print("______Empleado/s Contratados______")
        Empleado.mostrarnomytel(self)