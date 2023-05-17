from ManejadorFacultad import ListaFacultad

from ClaseMenu import Menu

if __name__ == '__main__':
    listafacu = ListaFacultad()
    listafacu.AbrirArchivo()
    #print(listafacu)
    unmenu = Menu()
    while True:
        print('\n-------Menu--------')
        print("1) - Mostrar Datos de la Facultad.")
        print("2) - Dado el nombre de la carrera, mostrar codigo, nombre y localidad de facultad")
        print("3) - Finalizar")
        opcion= input("\nIngrese la opcion Deseada: ")
        unmenu.opcion(opcion,listafacu)
