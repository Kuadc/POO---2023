

from ClaseNodo import Nodo

from zope.interface import implementer

from ClaseInterfaz import EjercicioInterface

from ClaseDocenteInvestigador import DocenteInvestigador

from ClaseInvestigador import Investigador

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
        self.__actual=nodo
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
    def ordenamientoporapellido(self):
        cabeza = self.__comienzo
        cota = None
        k = None
        while k != cabeza:
            k = cabeza
            p = cabeza
            while p.getSiguiente() != cota:
                if p.getDato().getApellido() > p.getSiguiente().getDato().getApellido():
                    aux = p.getSiguiente().getDato()
                    p.getSiguiente().setDato(p.getDato())
                    p.setDato(aux)
                    k = p
                else:
                    p = p.getSiguiente()
            cota = k.getSiguiente()

    def MostrarporCarrera(self,carrera):
        if isinstance(carrera,str):
            i=0
            tope = self.__tope
            aux = self.__comienzo
            while i<tope and aux != None:
                if isinstance(aux.getDato(),DocenteInvestigador):
                    if aux.getDato().getCarrera() == carrera:
                        print(aux.getDato())
                        aux = aux.getSiguiente()
                    else:
                        aux = aux.getSiguiente()
                else:
                    aux = aux.getSiguiente()
    def contaragente(self,area):
        i= 0
        contarI = 0
        contarDI = 0
        tope = self.__tope
        aux = self.__comienzo
        while i < tope and aux != None:
            if isinstance(aux.getDato(), DocenteInvestigador) and aux.getDato().getarea() == area:
                contarDI+=1
                aux = aux.getSiguiente()
                i=i+1
            elif isinstance(aux.getDato(), Investigador) and aux.getDato().getarea() == area:
                contarI += 1
                aux = aux.getSiguiente()
                i = i+1
            else:
                aux = aux.getSiguiente()
                i = i + 1
        print("Los docentes investigadores del Area informatica son:",contarDI)
        print("Los investigadores del Area informatica son:", contarI)

    def listarymostrarsueldo(self,cat):
        i = 0
        tope = self.__tope
        aux = self.__comienzo
        sueldototal = 0
        while i < tope and aux != None:
            if isinstance(aux.getDato(), DocenteInvestigador) and aux.getDato().getcategoria() == cat:
                #listar apellido, nombre e importe extra por docencia e investigació
                print(aux.getDato().mostrardatos())
                print("Importe extra por docencia: {}".format(aux.getDato().getimporteextradocencia()))
                print("Importe extra por investigacion: {}".format(aux.getDato().getimporteextrainvestigador()))
                sueldototal+= aux.getDato().getimporteextradocencia() + aux.getDato().getimporteextrainvestigador()
                i = i+1
                aux = aux.getSiguiente()
            else:
                i = i+1
                aux = aux.getSiguiente()
        print("El total del dinero que se debe solicitar es de : ",sueldototal)

    def ordenamiento(self):
        cabeza = self.__comienzo
        cota = None
        k = None
        while k != cabeza:
            k = cabeza
            p = cabeza
            while p.getSiguiente() != cota:
                if p.getDato().getnombre() > p.getSiguiente().getDato().getnombre():
                    aux =  p.getSiguiente().getDato()
                    p.getSiguiente().setDato(p.getDato())
                    p.setDato(aux)
                    k=p
                else:
                    p = p.getSiguiente()
            cota = k.getSiguiente()


    def sueldo(self):
        aux = self.__comienzo
        while aux != None:
            aux.getDato().mostrardatos()
            aux.getDato().mostrarsueldo()
            aux = aux.getSiguiente()


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


