from ClasePersonal import Personal


class Investigador(Personal):
    __area = ""
    __tipo = ""

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__area = kwargs['area']
        self.__tipo = kwargs['tipo']

    def __str__(self):
        return "%s \narea:%s \ntipo:%s" % (super().__str__(),self.__area,self.__tipo)

    def getApellido(self):
        return super().getApellido()

    def getarea(self):
        return self.__area

    def gettipo(self):
        return self.__tipo

    def getnombre(self):
        return super().getnombre()

    def mostrardatos(self):
        super().mostrardatos()
        print("Agente Investigador")

    def mostrarsueldo(self):
        antiguedad = (self.getsueldobasico() * ((self.getantiguedad() / 5)*5)) / 100
        sueldobasico = antiguedad + self.getsueldobasico()
        print("Sueldo Total del agente Investigador: ", sueldobasico)


    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil = super().getcuil(),
                apellido = super().getApellido(),
                nombre = super().getnombre(),
                sueldobasico = super().getsueldobasico(),
                antiguedad=super().getantiguedad(),
                area = self.__area,
                tipo = self.__tipo
            )
        )
        return d
