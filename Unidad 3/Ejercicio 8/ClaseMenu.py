

from ClaseDocente import Docente
from ClaseApoyo import Apoyo
from ClaseInvestigador import Investigador
from ClaseDocenteInvestigador import DocenteInvestigador

from zope.interface import Interface
from zope.interface import implementer


from ClaseDirector import IDirector

@implementer(IDirector)

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.opcion4,
                            '5':self.salir
                          }

    def opcion(self,op,lista):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='2' or op=="3" or op=='4':
            func(IDirector(lista))
        else:
            func()

    def opcion1(self,manejadordirector:IDirector):
        cuil = input("Ingrese cuil")
        basico = int(input("Ingrese nuevo basico"))
        manejadordirector.modificarBasico(cuil,basico)

    def opcion2(self,manejadordirector:IDirector):
        cuil = input("Ingrese cuil")
        porcentaje = int(input("Ingrese nuevo porcentaje"))
        manejadordirector.modificarPorcentajeporcargo(cuil,porcentaje)
        return
    def opcion3(self,manejadordirector:IDirector):
        cuil = input("Ingrese cuil")
        porcentaje = int(input("Ingrese nuevo porcentaje"))
        manejadordirector.modificarPorcentajeporcategoria(cuil,porcentaje)
        return
    def opcion4(self,manejadordirector:IDirector):
        cuil = input("Ingrese cuil")
        importe = int(input("Ingrese nuevo porcentaje"))
        manejadordirector.modificarImporteExtra(cuil,importe)
        return

    def salir(self):
        exit()


