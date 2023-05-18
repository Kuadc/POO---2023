from Manejadorhelado import listahelado

from Manejadorsabores import listasabores

if __name__ == "__main__":
    listasab = listasabores()
    listasab.abrirarchivo()
    print(listasab)
    listahe = listahelado()
    bandera = True
    while bandera :
        print("1 - Registrar un helado vendido ")
        print("2 - Mostrar el nombre de los 5 sabores de helado más pedidos")
        print("3 - Ingresar un número de sabor y estimar el total de gramos vendidos")
        print("4 - mostrar los sabores vendidos")
        print("5 - Total recaudado por la Heladería")
        print("6 - salir")
        op = int(input("Ingrese la opcion deseada, finalize con 6: "))
        if op == 1:
            #resgistrar un helado
            listahe.venderhelado(listasab)
            print("\n\n***Helado vendido**")
            print(listahe)
        elif op == 2:
            listahe.maspedidos(listasab)
        elif op == 3:
            print(listasab)
            listahe.buscarventa(listasab)
        elif op == 4:
            listahe.mostrarSaboresVendidos()
        elif op == 5:
            listahe.totalRecaudado()
        elif op == 6:
            print("----programa finalizado-----")
            bandera = False
