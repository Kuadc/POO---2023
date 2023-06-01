import csv

from ManejadorTaller import ArregloTaller

from ClasePersona import Persona

from ManejadorInscripcion import ListaInscripcion


def tamano():
    archivo = open("talleres.csv")
    reader = csv.reader(archivo, delimiter=";")
    d = next(reader)
    dim = int(d[0])
    archivo.close()
    return dim


if __name__ == '__main__':
    dimension = tamano()
    arregloTaller = ArregloTaller(dimension)
    arregloTaller.abrirarchivo()
    arregloinsc = ListaInscripcion(5,5)
    bandera = True
    while bandera:
        print("1- Inscribir una persona")
        print("2- Consultar Inscripcion")
        print("3- Consultar Inscriptos")
        print("4- Registrar pago")
        print("5- Guardar inscripciones")
        print("6- Salir")
        op = int(input("Ingrese la opcion deseada: "))
        if op == 1:
            persona1= Persona("Carlos","mendoza 331 (s)","29345428")
            persona2= Persona("Mariana","Av. Libertador 1300 (n)","25989332")
            print("\n 1- Inscribiendo una persona \n")
            arregloTaller.inscribirpersona(persona1,"18/05/2023",arregloinsc)
            print("\n 1- Inscribiendo otra persona \n")
            arregloTaller.inscribirpersona(persona2,"30/05/2023",arregloinsc)

        elif op == 2:
            dni = input("Ingrese dni a consultar: ")
            arregloinsc.buscardni(dni)

        elif op == 3:
            arregloTaller.buscarincriptos()
        elif op == 4:
            dni = input("Ingrese dni a cambiar: ")
            arregloinsc.cambiarestadodni(dni)
        elif op == 5:
            arregloinsc.guardarenarchivo()
        else:
            print("Saliendo del programa.......")
            bandera = False

