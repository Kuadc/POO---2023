import csv

from ManejadorTaller import ArregloTaller

from ClasePersona import Persona

from ManejadorInscripcion import Inscripcion


def tamano():
    archivo = open("talleres.csv")
    reader = csv.reader(archivo, delimiter=",")
    d = next(reader)
    dim = d[0]
    archivo.close()
    return dim


if __name__ == '__main__':
    dimension = tamano()
    arregloTaller = ArregloTaller(dimension)
    arregloTaller.abrirarchivo()
    arregloinsc = Inscripcion(5,5)
    persona1= Persona("Carlos","mendoza 331 (s)","29345428")
    persona2= Persona("Mariana","Av. Libertador 1300 (n)","25989332")
    print("\n 1- Inscribiendo una persona \n")
    arregloTaller.inscribirpersona(persona1,"18/05/2023",arregloinsc)
    print("2- Consultar Inscripcion")
    dni = input("Ingrese dni a consultar: ")
    arregloTaller.buscarpersona(dni) #cambiarlos por buscar en el arreglo de inscriptos
    print("3- Consultar Inscriptos")
    arregloTaller.buscarincriptos()
    print("4- Registrar pago")
    dni = input("Ingrese dni a cambiar: ")
    arregloinsc.cambiarestadodni(dni)
    print("5 - Guardando inscriptiones.....-->")
    arregloinsc.guardarenarchivo()
