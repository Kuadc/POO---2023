

from ClaseNodo import Nodo

from zope.interface import implementer

from ClaseInterfaz import EjercicioInterface

from ClaseTesorero import ITesorero

from ClaseDirector import IDirector

from ClaseDocenteInvestigador import DocenteInvestigador

from ClaseInvestigador import Investigador

from ClaseApoyo import Apoyo

from ClaseDocente import Docente

@implementer(ITesorero)
@implementer(IDirector)
@implementer(EjercicioInterface)
class Lista:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None

    def AgregarElemento(self, elemento):
        nodo = Nodo(elemento)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual= nodo
        self.__tope+=1

    def InsertarElemento(self,elemento,pos):
        if pos == 0:
            self.AgregarElemento(elemento)
        else:
            i=0
            aux = self.__comienzo
            anterior = self.__comienzo
            while i<pos and aux != None: # inicializamos i en 0 para recorrer la lista de nodos
                anterior = aux
                aux = aux.getSiguiente()
                i+=1
            if pos == i:  #encontro la posicion
                nodo = Nodo(elemento) #creo el nuevo nodo
                anterior.setSiguiente(nodo) #al nodo anterior le enlazo el nuevo nodo
                nodo.setSiguiente(aux) #y al nodo nuevo le enlazo el nodo siguiente.
                self.__tope+=1 #aumento el tope

            else:
                raise IndexError
    #metodo de la clase ITesorero
    def gastosSueldoPorEmpleado(self, cuil):
        i = 0
        tope = self.__tope
        aux = self.__comienzo
        while i < tope and aux != None:
            if cuil == aux.getDato().getcuil():
                aux.getDato().mostrarsueldo()
                i = tope
            else:
                i=i+1
                aux = aux.getSiguiente()


    #metodos de  la clased IDirector
    def modificarBasico(self,cuil,nuevobasico):
        i = 0
        aux = self.__comienzo
        bandera = False
        while not bandera and aux != None:
            if cuil == aux.getDato().getcuil():
                print("Basico actual:", aux.getDato().getbasico())
                aux.getDato().modificarbasico(nuevobasico)
                print("___Basico cambiado___")
                print("Nuevo Basico:",aux.getDato().getbasico())
                bandera = True
            else:
                aux = aux.getSiguiente()
        if bandera == False:
            print("Agente no encontrado")
        return

    def modificarPorcentajeporcargo(self,cuil,nuevoPorcentaje):
        aux = self.__comienzo
        bandera = False
        while not bandera and aux != None:
            if cuil == aux.getDato().getcuil() and isinstance(aux.getDato(),Docente):
                print("Porcentaje Actual: ",aux.getDato().getporcentaje())
                aux.getDato().cambiarporcentaje(nuevoPorcentaje)
                print("___Porcentaje cambiando___")
                print("Nuevo porcentaje:",aux.getDato().getporcentaje())
                bandera = True

            else:
                aux = aux.getSiguiente()

        if bandera == False:
            print("Docente no encontrado")
        return

    def modificarPorcentajeporcategoria(self,cuil,nuevoPorcentaje):
        aux = self.__comienzo
        bandera = False
        while not bandera and aux != None:
            if cuil == aux.getDato().getcuil() and isinstance(aux.getDato(),Apoyo):
                print("Porcentaje Actual: ",aux.getDato().getporcentaje())
                aux.getDato().cambiarporcentaje(nuevoPorcentaje)
                print("___Porcentaje cambiando___")
                print("Nuevo porcentaje:",aux.getDato().getporcentaje())
                bandera = True
            else:
                aux = aux.getSiguiente()
        if bandera == False:
            print("Agente no encontrado")
        return

    def modificarImporteExtra(self,cuil,nuevoImporteExtra):
        i = 0
        aux = self.__comienzo
        bandera = False
        while not bandera and aux != None:
            if cuil == aux.getDato().getcuil() and isinstance(aux.getDato(),DocenteInvestigador):
                aux.getDato().cambiarimporteextra(nuevoImporteExtra)
                print("___Porcentaje cambiando___")
                bandera = True
            else:
                aux = aux.getSiguiente()
        if bandera == False:
            print("Agente no encontrado")
        return

    def getTope(self):
        return self.__tope

    def MostrarElemento(self,pos):
        if isinstance(pos,int):
            i=0
            aux = self.__comienzo
            while i<pos and aux != None:
                aux = aux.getSiguiente()
                i+=1
            if pos == i:
                print(aux.getDato())
            else:
                raise IndexError
    def toJSON(self):
            d = dict(
            __class__ = self.__class__.__name__,
            Personal = [nodo.toJSON() for nodo in self]
            )
            return d

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato


