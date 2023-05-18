

class helado:
    __gramos = 0
    __precio = 0
    __sabores = []

    def __init__(self,gramos,precio,listasabores):
        self.__gramos = gramos
        self.__precio = precio
        self.__sabores = []
        for sabor in listasabores:
            self.__sabores.append(sabor)

    def mostrarhelado(self):
        print("gramos: %s , precio: %s,"%(self.__gramos,self.__precio))
        for i in range(len(self.__sabores)):
            self.__sabores[i].mostrarsabores()
        
    def __str__(self):
        s=""
        s+="Gramos: %s - Precio:%s" %(self.__gramos,self.__precio)
        for sabor in self.__sabores:
            s+=str(sabor)+"\n"
        return s
    
    def Getprecio(self):
        return self.__precio
    
    def getgramos(self):
        return self.__gramos
    
    def Getlistasabores(self):
        return self.__sabores