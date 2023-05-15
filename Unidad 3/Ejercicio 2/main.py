from Manejadorhelado import listahelado

from Manejadorsabores import listasabores

if __name__ == "__main__"
    listasab = listasabores()
    listasab.abrirarchivo()
    listahe = listahelado()
    op = int(input("Ingrese la opcion deseada, finalize con 0: "))
    while op !=0 :
        print("1 - opcion uno")
        print("2 - opcion uno")
        print("3 - opcion uno")
        print("4 - opcion uno")
        print("5 - opcion uno")
        if op == 1:
            #resgistrar un helado
            listahe.venderhelado(listasab)

