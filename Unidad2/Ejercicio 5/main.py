from Listaplan import lista
from Plan import PlanAhorro
from claseMenu import Menu

if __name__ == "__main__": 
    unalista = lista()
    unalista.cargararchivo()
    #print(unalista)
    #PlanAhorro.vercuotas()
    opcionmenu = Menu()
    while True:
               print('\n-------Menu--------')
               print("1) - Actualizar el valor del vehículo de cada planr.")
               print("2) - Dado un valor, mostrar código del plan, modelo y versión del vehículo.")
               print("3) - Mostrar el monto que se debe haber pagado para licitar el vehículo")
               print("4) - Modificar la cantidad cuotas que debe tener pagas para licitar.")
               print("5) - Finalizar.")
               opcion= input("\nIngrese la opcion Deseada: ")
               opcionmenu.opcion(opcion,unalista)
               
