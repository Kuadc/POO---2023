from ClasePersonal import Personal

class Docente(Personal):
    __cargo = ""
    __catedra = ""
    __carrera = ""
    __porcentaje = 0

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__cargo = kwargs['cargo']
        self.__catedra = kwargs['catedra']
        self.__carrera = kwargs['carrera']
        self.__porcentaje = int(kwargs['porcentaje'])

    def __str__(self):
        return "%s \ncargo:%s \ncatedra:%s \ncarrera:%s" % (super().__str__(),self.__cargo,self.__catedra,self.__carrera)

    def getApellido(self):
        return super().getApellido()
    def getCarrera(self):
        return self.__carrera
    def getcargo(self):
        return self.__cargo
    def cambiarporcentaje(self,porcentaje):
        self.__porcentaje = porcentaje

    def getporcentaje(self):
        return self.__porcentaje
    def getcuil(self):
        return super().getcuil()

    def modificarbasico(self,basico):
        super().modificarbasico(basico)

    def getbasico(self):
        return super().getbasico()


    def getnombre(self):
        return super().getnombre()
    def getcatedra(self):
        return self.__catedra

    def mostrardatos(self):
        super().mostrardatos()
        print("Agente Docente")

    def mostrarsueldo(self):
        antiguedad = (self.getsueldobasico() * ((self.getantiguedad() / 5)*5)) / 100
        sueldobasico = self.getsueldobasico()+antiguedad
        if self.__cargo == "simple":
            sueldobasico+=self.getsueldobasico()+0.10
        elif self.__cargo == "semiexclusivo":
            sueldobasico += self.getsueldobasico() + 0.20
        elif self.__cargo == "exclusivo":
            sueldobasico += self.getsueldobasico() + 0.50

        print("Sueldo basico Agente: ", sueldobasico)

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil = super().getcuil(),
                apellido = super().getApellido(),
                nombre = super().getnombre(),
                sueldobasico = super().getsueldobasico(),
                antiguedad=super().getantiguedad(),
                cargo = self.__cargo,
                catedra = self.__catedra,
                carrera = self.__carrera
            )
        )
        return d
