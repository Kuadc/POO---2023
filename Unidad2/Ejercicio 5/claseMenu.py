import sys

from Plan import PlanAhorro
"""from ListaViajero import lista"""

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
        if op=='1' or op=='2' or op=="3":
            func(lista)
        else:
            func()

    def salir(self):
        print('Usted salio del programa')
        sys.exit(0)
        

    def opcion1(self,lista):
        lista.ModificarValor()
        """Actualizar el valor del vehículo de cada plan. Para esto se muestra 
        el código del plan, el modelo y versión del vehículo, luego se ingresa 
        el valor actual del vehículo y se modifica el atributo correspondiente."""
    
    def opcion2(self,lista):
       """Dado un valor, mostrar código del plan, modelo y versión del vehículo 
       cuyo valor de la cuota sea inferior al valor dado."""
       valor = float(input("Ingrese el valor de la cuota: "))
       lista.BuscarCuotaInferior(valor)
        

    def opcion3(self,lista):
        """Mostrar el monto que se debe haber pagado para licitar el vehículo
        (cantidad de cuotas para licitar * importe de la cuota)."""
        lista.BuscarMontoLicitacion()

    def opcion4(self,lista):
        PlanAhorro.Cambiarvariables()
        return 
        