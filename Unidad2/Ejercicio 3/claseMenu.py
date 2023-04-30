

"""from ListaViajero import lista"""

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.salir
                          }

    def opcion(self,op,lista):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='2' or op=="3":
            func(lista)
        else:
            func()

    def salir(self):
        print('Usted salio del programa')

    def opcion1(self,lista):
        # Mostrar para cada variable el día y hora de menor y mayor valor.
        lista.mostrarmayortemp()
        lista.mostrarmayorhumedad()
        lista.mostrarmayorpresion()

    def opcion2(self,lista):
        #Indicar la temperatura promedio mensual por cada hora.
        lista.promediomensual()
        

    def opcion3(self,lista):
        #Dado un número de día listar los valores de las tres variables para cada hora del día dado
        dia = int(input("Ingrese un numero de dia: "))
        lista.mostrarvariables(dia)
        