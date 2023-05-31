from ClasePersonal import Personal
from ClaseDocente import Docente
from ClaseInvestigador import Investigador


class DocenteInvestigador(Docente,Investigador):
    __categoria = 0
    __importeextradocencia = 0
    __importeextrainvestigador = 0

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__categoria = int(kwargs['categoria'])
        self.__importeextradocencia = int(kwargs['importeextradocencia'])
        self.__importeextrainvestigador = int(kwargs['importeextrainvestigador'])

    def __str__(self):
        return "%s \nCategoria:%s \nImporte Extra Docencia: %s \nImporte Extra Investigador: %s" % (super().__str__(),self.__categoria, self.__importeextradocencia,self.__importeextrainvestigador)

    def getApellido(self):
        return super().getApellido()
    
    def getnombre(self):
        return super().getnombre()

    def getCarrera(self):
        return super().getCarrera()

    def getarea(self):
        return super().getarea()

    def getcategoria(self):
        return self.__categoria

    def mostrardatos(self):
        Personal.mostrardatos(self)
        print("Agente Docente Investigador")
    
    def getimporteextradocencia(self):
        return self.__importeextradocencia

    def mostrarsueldo(self):
        super().mostrarsueldo()
        sueldo =
        print("Sueldo Total del agente Docente-Investigador: ", sueldobasico)
    
    def getimporteextrainvestigador(self):
        return self.__importeextrainvestigador

    def getsueldobasico(self):
        return super().getsueldobasico()
    
    def getantiguedad(self):
        return super().getantiguedad()
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil = super().getcuil(),
                apellido = super().getApellido(),
                nombre = super().getnombre(),
                sueldobasico = super().getsueldobasico(),
                area = super().getarea(),
                tipo = super().gettipo(),
                cargo = super().getcargo(),
                catedra = super().getcatedra(),
                carrera = super().getCarrera(),
                antiguedad = super().getantiguedad(),
                categoria = self.__categoria,
                importeextradocencia = self.__importeextradocencia,
                importeextrainvestigador = self.__importeextrainvestigador
            )
        )
        return d
