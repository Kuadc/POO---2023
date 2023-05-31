from ClasePersonal import Personal

class Apoyo(Personal):
    __categoria = 0

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__categoria = kwargs['categoria']

    def __str__(self):
        return "%s \nCategoria: %s" % (super().__str__(), self.__categoria)

    def getApellido(self):
        return super().getApellido()

    def getnombre(self):
        return super().getnombre()

    def mostrardatos(self):
        super().mostrardatos()
        print("Agente Apoyo")

    def mostrarsueldo(self):
        antiguedad = (self.getsueldobasico()*(self.getantiguedad()/5))/100
        sueldobasico = self.getsueldobasico()+antiguedad+(self.getsueldobasico()*0.10)
        print("Sueldo basico Agente Apoyo: ",sueldobasico)

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=super().getcuil(),
                apellido=super().getApellido(),
                nombre=super().getnombre(),
                sueldobasico=super().getsueldobasico(),
                antiguedad = super().getantiguedad(),
                categoria = self.__categoria
            )
        )
        return d