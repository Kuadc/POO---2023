
from menu import Menu
from conjunto import ClaseConjunto

if __name__ == "__main__":
    print("**Conjunto A**\n")
    A = ClaseConjunto()
    A.Agregarelementos()
    print("**\n Conjunto B**\n")
    B = ClaseConjunto()
    B.Agregarelementos()
    print("\n*** Conjuntos creados ***\n")
    print("Conjunto A: ", A)
    print("Conjunto B:", B)
    unmenu = Menu()
    while True:
        print("1 - Union de 2 conjuntos")
        print("2 - Diferencia de 2 conjuntos")
        print("3 - Verificar si 2 conjuntos son iguales")
        print("4 - Salir")
        opcion = input("Ingrese la opcion deseada")
        unmenu.opcion(opcion, A, B)
