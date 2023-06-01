import csv

from ClasePersona import Persona


class ListaPersona:
    __lista = []

    def __init__(self):
        self.__lista = []

    def guardarpersona(self,persona):
        self.__lista.append(persona)

