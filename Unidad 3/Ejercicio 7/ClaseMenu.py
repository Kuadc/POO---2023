from ClaseDocenteInvestigador import DocenteInvestigador

from ClaseDocente import Docente
from ClaseApoyo import Apoyo
from ClaseInvestigador import Investigador
from ClaseDocenteInvestigador import DocenteInvestigador

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.opcion4,
                            '5':self.opcion5,
                            '6':self.opcion6,
                            '7':self.opcion7,
                            '8':self.opcion8,
                            '9':self.opcion9,
                            '10':self.salir
                          }

    def opcion(self,op,lista,jsonf):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='2' or op=="3" or op=='4' or op=='5' or op=='6' or op=='7'  or op=='8' or op=='9':
            func(lista,jsonf)
        else:
            func()

    def opcion1(self,lista,jsonf):
        # Insertar un agente en una posición determinada
        print("Agregando un Docente investigador")
        pos = int(input("Igrese la posicion donde desea agregar el agente: "))
        dic = {'cuil': '285553334', 'apellido': 'Carrizo', 'nombre': 'Efrain', 'sueldobasico': '200000',
                'antiguedad': '15', 'area': 'Ciencias', 'tipo': 'Academico', 'cargo': 'Titular', 'catedra': 'Astromomia',
                'carrera': 'Atronomo', 'categoria': '1', 'importeextradocencia': '5000', 'importeextrainvestigador': '6000'}
        unagente = DocenteInvestigador(**dic)
        try:
            lista.InsertarElemento(unagente,pos)
        except IndexError:
            print("\n !Cuidado! - La posicion del elemento no es valida\n")

    def opcion2(self,lista,jsonf):
        #agregar un agente a la coleccion
        print("1 - Personal de apoyo")
        print("2 - Personal Docente")
        print("3 - Personal Investigador")
        print("4 - Personal Docente-Investigador")
        agente = int(input("Ingrese el tipo de agente que desea agregar: "))
        if agente == 1:
            dic = {'cuil': '204441112', 'apellido': 'Maffezini', 'nombre': 'Marcos', 'sueldobasico': '80000',
                    'antiguedad': '10', 'categoria': '7'}
            unagente = Apoyo(**dic)
            lista.AgregarElemento(unagente)
        elif agente == 2:
            dic = {'cuil': '2734544267', 'apellido': 'Sanchez', 'nombre': 'Miguel', 'sueldobasico': '70000',
                    'antiguedad': '7', 'cargo': 'JTP', 'catedra': 'POO', 'carrera': 'LCC'}
            unagente = Docente(**dic)
            lista.AgregarElemento(unagente)
        elif agente == 3:
            dic = {'cuil': '2089574631', 'apellido': 'Baccalara', 'nombre': 'Rodolfo', 'sueldobasico': '97000',
                    'antiguedad': '15', 'area': 'Informatica', 'tipo': 'Indendiente'}
            unagente = Investigador(**dic)
            lista.AgregarElemento(unagente)
        elif agente == 4:
            dic = {'cuil': '2067452910', 'apellido': 'Figueroa', 'nombre': 'Agustin', 'sueldobasico': '1500000',
                    'antiguedad': '14', 'area': 'Informatica', 'tipo': 'Academico', 'cargo': 'Titular',
                    'catedra': 'Procedural', 'carrera': 'TUPW', 'categoria': '1', 'importeextradocencia': '5000',
                    'importeextrainvestigador': '6000'}
            unagente = DocenteInvestigador(**dic)
            lista.AgregarElemento(unagente)
        else:
            print("Ingreso erroneo, intente nuevamente")


    def opcion3(self,lista,jsonf):
        #Dada una posición de la Lista: Mostrar el agente
        pos = int(input("Ingrese la posicion del agente que desea mostrar:"))
        try:
            lista.MostrarElemento(pos)
        except IndexError:
            print("\nLa posicion enviada no es correcta o no existe el elemento alguno en esa posicion\n")


    def opcion4(self,lista,jsonf):
        #Ingresar por teclado el nombre de una carrera y generar un listado ordenado por apellido con todos los datos de los agentes que se desempeñan como docentes investigadores.
        carrera  = input("Ingrese el nombre de la carrera")
        lista.ordenamiento()
        lista.MostrarporCarrera(carrera)

    def opcion5(self,lista,jsonf):
        try:
            lista.contaragente("Informatica")
        except IndexError:
            print("\n No hay areas de informatica\n")

    def opcion6(self,lista,jsonf):
        lista.ordenamientoporapellido()
        lista.sueldo()


    def opcion7(self,lista,jsonf):
        categoria = int(input("Ingrese una categoria del 1 al 5"))
        lista.listarymostrarsueldo(categoria)



    def opcion8(self,lista,jsonf):
        d = lista.toJSON()
        jsonf.guardarJSONArchivo(d, 'personal2.json')

    def opcion9(self,lista,jsonf):
        for dato in lista:
            print(dato)

    def salir(self):
        exit()


