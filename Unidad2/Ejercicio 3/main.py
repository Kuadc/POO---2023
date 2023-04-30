from Listaregisro import lista
from claseMenu import Menu

if __name__ == "__main__": 
    unalista = lista()
    unalista.cargararchivo()
    opcionmenu = Menu()
    while True:
               print('\n-------Menu--------')
               print("1) - Mostrar para cada variable el día y hora de menor y mayor valor.")
               print("2) - Indicar la temperatura promedio mensual por cada hora.")
               print("3) -  Dado un número de día listar los valores de las tres variables para cada hora del día dado")
               print("4) - Finalizar")
               opcion= input("\nIngrese la opcion Deseada: ")
               opcionmenu.opcion(opcion,unalista)
               
