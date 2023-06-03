from ClaseObjectEncoder import ObjectEncoder
from ClaseLista import Lista
from ClaseMenu import Menu
from zope.interface import Interface
from zope.interface import implementer
from ClaseTesorero import ITesorero

@implementer(ITesorero)


def tesorero(manejarTesorero:ITesorero):
    cuil = input("Ingrese cuil")
    manejarTesorero.gastosSueldoPorEmpleado(cuil)
    return

if __name__ == "__main__":
    jsonF = ObjectEncoder()
    lista = Lista()
    diccionario=jsonF.leerJSONArchivo('personal.json')
    lista = jsonF.decodificarDiccionario(diccionario)
    menu = Menu()
    bandera = True
    usuario = input('Ingrese el Usuario (Director/Tesorero): ').lower()
    clave = input('Ingrese Clave:')
    while bandera:
        if usuario == "tesorero" and clave == "ufC77#!1":
            print("Gastos en conceptos de sueldos")
            tesorero(ITesorero(lista))
        elif usuario == "director" and clave == "ag@74ck":
            print("1 - Modificar el basico del agente")
            print("2 - Modificar el porcenaje por cargo docente")
            print("3 - Modificar porcentaje que se paga por categoría a un personal de apoyo")
            print("4 - Modificar importe extra que se paga a un docente investigador")
            print("5 - Salir")
            opcion = input("Ingrese el la opcion deseada: ")
            menu.opcion(opcion, lista)

