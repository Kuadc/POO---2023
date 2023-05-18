import csv

from Clasehelado import helado

from clasesabores import sabores

class listahelado:
    __listahelado = []

    def __init__(self):
        self.__listahelado= []

    def venderhelado(self,listasab):
        cantidad = self.listarheladosengramos()
        precio = self.precioshelados(cantidad)
        lista = self.elejirsabores(listasab)
        unhelado = helado(cantidad,precio,lista)
        self.__listahelado.append(unhelado)

    def listarheladosengramos(self):
        print("1 - Helado de 100 grs")
        print("2 - Helado de 150 grs")
        print("3 - Helado de 250 grs")
        print("4 - Helado de 500 grs")
        print("5 - Helado de 1000 grs")
        cantidad = int(input("Ingrese el helado en gramos:"))
        return cantidad

    def precioshelados(self,cantidad):
        if cantidad == 100:
            precio = 300
        elif cantidad == 150:
            precio = 450
        elif cantidad == 150:
            precio = 600
        elif cantidad == 500:
            precio = 1200
        else:
            precio = 2000
        return precio
    
    def elejirsabores(self,listasab):
        cant = int(input("\nIgrese la cantidad de sabores: \n"))
        lista = []
        for i in range(cant):
            print(listasab)
            indice = int(input("Ingrese el codigo de sabor n°%s: "%(i+1)))
            sabor = listasab.buscarsabor(indice-1)
            lista.append(sabor)
        return lista
    
    def maspedidos(self,listasab):
        i=0
        lista = [0 for i in range(9)]
        j = 0
        while i<len(self.__listahelado):
            listasabores = self.__listahelado[i].Getlistasabores()
            while j<len(listasabores):
                indice = listasabores[j].getcodigo()
                listasabores[indice-1]+=1                    
                j= j+1
            i=i+1
        indices = self.listademaspedidos(lista)
        listasab.mostrarsabores(indices)
        return
    
    def listademaspedidos(self,lista):
        indices = list(enumerate(lista))
        indices.sort(key=lambda x: x[1], reverse=True)
        i=0
        ind = []
        while i<5:
            ind.append(indices[i][0])
            i=i+1
        return ind
    
    def buscarventa(self,listasab):
        cod = int(input("Ingrese el codigo del sabor: "))
        i=0
        lista = [0 for i in range(9)]
        j = 0
        acumulador = 0
        while i<len(self.__listahelado):
            listasabores = self.__listahelado[i].Getlistasabores()
            while j<len(listasabores):
                if cod == listasabores[j].getcodigo():
                    sabores = len(listasabores)
                    gramos = self.__listahelado[i].getgramos()/sabores
                    acumulador = acumulador + gramos
                    j=j+1
                else: j=j+1
            i = i+1
            j = 0
        listasab.mostrarsabor(cod)
        print("total de gramos vendidos: ",acumulador)
        
    def mostrarSaboresVendidos(self):
        i = 0
        j = 0
        while i<len(self.__listahelado):
            listasabores = self.__listahelado[i].Getlistasabores()
            while j<len(listasabores):
                print(listasabores[j])
                j=j+1
            j=0
            i=i+1
            
    def totalRecaudado(self):
        i=0
        acumulador = 0
        while i<len(self.__listahelado):
            precio = self.__listahelado[i].Getprecio()
            acumulador = acumulador +precio
            i=i+1
        print("Total recaudado por la heladeria: ", acumulador)
        
    def __str__(self):
        s = ""
        for helado in self.__listahelado:
            s+= str(helado) + "\n"
        return s