import json

class Nodo:
    __agentes=None
    __siguiente=None

    def __init__(self, unagente):
        self.__agentes=unagente
        self.__siguiente=None

    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente

    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__agentes

    def setDato(self,nodo):
        self.__agentes = nodo

    def toJSON(self):
        d = dict(
        __class__=self.__class__.__name__,
        __atributos__=dict(
        personal = self.__agentes.toJSON()
        ))
        return d
