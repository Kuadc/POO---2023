from ArregloEmpleados import Arreglo

from ClaseMenu import Menu

if __name__ == '__main__':
    dimension = int(input("Ingrese la cantidad de empleados: "))
    unarreglo  = Arreglo(dimension)
    unarreglo.abrirplanta()
    unarreglo.abrircontratado()
    unarreglo.abrirexterno()
    #unarreglo.mostrardatos()
    unmenu = Menu()
    while True:
        print('\n-------Menu--------')
        print("1) - Registrar Horas.")
        print("2) - Total de la Tarea")
        print("3) - Ayuda Económica")
        print("4) - Calcular Sueldo")
        print("5) - Finalizar")
        opcion= input("\nIngrese la opcion Deseada: ")
        unmenu.opcion(opcion,unarreglo)
