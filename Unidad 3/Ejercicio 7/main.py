from ClaseObjectEncoder import ObjectEncoder
from ClaseLista import Lista
from ClaseMenu import Menu

from ClaseApoyo import Apoyo
from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClaseDocenteInvestigador import DocenteInvestigador

if __name__ == "__main__":
    jsonF = ObjectEncoder()
    lista = Lista()
    diccionario=jsonF.leerJSONArchivo('personal.json')
    lista = jsonF.decodificarDiccionario(diccionario)
    menu = Menu()
    bandera = True
    while bandera:
        print("1) - Insertar a agentes en la colección en una posición determinada.")
        print("2) - Agregar un agente a la colección")
        print("3) - Dada una posición de la Lista: Mostrar el agente")
        print("4) - Ingresar una carrera y mostrar los docentes investigadores ordenados.")
        print("5) - Dado una area de investigacion, contar los docentes_investigador y investigadores .")
        print("6) - Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.")
        print("7) - Dada una categoria de investigacion, listar cuanto se debe pagar por docente_investigador")
        print("8) - Almacenar los datos de todos los agentes en el archivo “personal.json”  ")
        print("9) - Mostrar lista”  ")
        print("10) - salir")
        opcion = input("Ingrese el la opcion deseada: ")
        menu.opcion(opcion, lista, jsonF)
