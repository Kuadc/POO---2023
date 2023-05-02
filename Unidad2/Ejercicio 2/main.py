
from ListaViajero import lista
from claseMenu import Menu

if __name__ == "__main__": 
    unalista = lista()
    unalista.cargararchivo()
    numviajero= int(input("Ingrese su numero de viajero frecuente: "))
    indice = unalista.buscarviajero(numviajero)
    if indice == None:
        print("viajero no encontrado")
    else: 
        opcionmenu = Menu()
        while True:
               print('\n-------Menu--------')
               print("1) - Consultar Cantidad de Millas.")
               print("2) - Acumular Millas.")
               print("3) - Canjear Millas")
               print("4) - Finalizar")
               opcion= input("\nIngrese la opcion Deseada: ")
               opcionmenu.opcion(opcion,unalista,indice)
