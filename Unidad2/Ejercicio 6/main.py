
from ListaViajero import lista

if __name__ == "__main__": 
    unalista = lista()
    unalista.cargararchivo()
    millas = unalista.cantidadMillas()
    unalista.buscarViajeros(millas)
    print("\n Ahora utilizaremos la sobrecarga del operador suma")
    num = int(input("Ingrese el numero de viajero frecuente: "))
    acumularM = int(input("Ingrese la cantidad de millas a acumular: "))
    unalista.AcumularMillas(num,acumularM)
    print("\n Ahora utilizaremos la sobrecarga del operador resta")
    num = int(input("Ingrese el numero de viajero frecuente: "))
    acumularM = int(input("Ingrese la cantidad de millas a restar: "))
    unalista.restarMillas(num,acumularM)
