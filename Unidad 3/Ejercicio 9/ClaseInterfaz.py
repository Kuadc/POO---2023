from zope.interface import Interface


class EjercicioInterface(Interface):

    def InsertarElemento(elemento,posicion):
        pass

    def AgregarElemento(elemento):
        pass

    def MostrarElemento(posicion):
        pass
