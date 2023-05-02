

"""from ListaViajero import lista"""

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.salir
                          }

    def opcion(self,op,lista,indice):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='2' or op=="3":
            func(lista,indice)
        else:
            func()

    def salir(self):
        print('Usted salio del programa')

    def opcion1(self,lista,indice):
        # Consultar Cantidad de Millas.
        totalmillas=lista.cambiarMillas(indice)
        print("Total de millas acumuladas: ", totalmillas)

    def opcion2(self,lista,indice):
        #Acumular Millas.
        millas = int(input("Ingrese la cantidad de millas recorridas: "))
        millasacumuladas = lista.acumular_millas(indice,millas)
        print("Total de millas acumuladas: ", millasacumuladas)
        

    def opcion3(self,lista,indice):
        #Canjear Millas.
        canjemillas = int(input("Ingrese la cantidad de milllas a canjear: "))
        millasrestantes = lista.canjearMillas(indice,canjemillas)
        print("Total de millas en la actualidad: ", millasrestantes)