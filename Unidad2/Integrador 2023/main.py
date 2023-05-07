from ManejadorAlumnos import ArregloAlumnos

from ManejadorMaterias import ListaMateria

from ClaseMenu import Menu

if __name__ == '__main__':
    unalista = ListaMateria()
    unalista.AbrirArchivo()
    #print(unalista)
    arreglo = ArregloAlumnos(5,5)
    arreglo.AbrirArchivo()
    #arreglo.mostrardatos()
    unmenu = Menu()
    while True:
        print("\n ****____Menu de opciones____****\n")
        print("1 - Informar promedio y aplazos")
        print("2 - Promocional")
        print("3 - Listado de alumnos")
        print("4 - Salir")
        op = input("Ingrese la opcion deseada: ")
        unmenu.opcionmenu(op,unalista,arreglo)
