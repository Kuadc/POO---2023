
class Taller:
    __idtaller = 0
    __nombre = ""
    __vacantes = 0
    __montoinscripcion = 0
    __lista = []

    def __init__(self, idtaller, nombre, vacantes, monto):
        self.__idtaller = idtaller
        self.__nombre = nombre
        self.__vacantes = vacantes
        self.__montoinscripcion = monto
        self.__lista = []

    def __str__(self):
        return "Codigo: %s Nombre:%s Monto:%s" % (self.__idtaller, self.__nombre, self.__montoinscripcion)

    def nuevainscripcion(self, inscripcion):
        self.__lista.append(inscripcion)

    def modificarvacante(self):
        self.__vacantes -= 1

    def Getvacantes(self):
        return self.__vacantes

    def Getcodtaller(self):
        return self.__idtaller

    def getmontoinscripcion(self):
        return self.__montoinscripcion

    def mostrarpersonas(self):
        i=0
        while i< len(self.__lista): #en esta lista tengo todas las inscripiones a dicho taller
            persona = self.__lista[i].Getpersona()
            print(persona)
            i=i+1

    def mostrartaller(self):
        print("Nombre del taller:{} ".format(self.__nombre))

