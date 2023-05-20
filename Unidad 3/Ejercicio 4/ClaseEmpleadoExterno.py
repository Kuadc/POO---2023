import datetime

from ClaseEmpleado import Empleado


'''Sueldo = costo de la obra - viático- monto del seguro de vida'''


class EmpleadoExterno(Empleado):
    __tarea = ""
    __fechainicio = ""
    __fechafinalizacion = ""
    __viatico = 0
    __costo = 0
    __montoseguro = 0

    def __init__(self, **kwargs):
        Empleado.__init__(self,**kwargs)
        self.__tarea = kwargs['tarea']
        self.__fechainicio = kwargs['fechainicio']
        self.__fechafinalizacion = kwargs['fechafinalizacion']
        self.__viatico = kwargs['viatico']
        self.__costo = kwargs['costo']
        self.__montoseguro = kwargs['montoseguro']

    def __str__(self):
        fechfin = self.__fechafinalizacion.strftime('%d/%m/%Y')
        cadena = ' ______Empleado Externo_________\n '
        cadena+='DNI: {} \n Nombre:{} \n Direccion: {} \n Telefono: {} '.format(self.getdni(),self.getnombre(),self.getdireccion(),self.gettelefono())
        cadena+='\n Tarea:{}\n Fecha Inicio:{}\n Fecha Finalizacion:{}\n Viatico:{}\n Costo Obra:{}\n Monto del Seguro:{}'.format(self.__tarea,self.__fechainicio,fechfin,self.__viatico,self.__costo,self.__montoseguro)
        return cadena

    def gettarea(self):
        return self.__tarea

    def getfechafinalizacion(self):
        return self.__fechafinalizacion

    def getviatico(self):
        return self.__viatico

    def getcosto(self):
        return self.__costo

    def getmontoseguro(self):
        return self.__montoseguro

    def calcularsueldo(self):
        sueldo = (self.__costo - self.__viatico)-self.__montoseguro
        return sueldo
    def mostrarnomytel(self):
        print("______Empleado/s Externos______")
        Empleado.mostrarnomytel(self)