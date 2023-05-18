
class sabores:
    __codigo = 0
    __ingredientes = ""
    __sabor = ""

    def __init__(self,cod,ingre,sabor):
        self.__codigo = cod
        self.__ingredientes = ingre
        self.__sabor = sabor

    def mostrarsabor(self):
        print("codigo: %s \t sabor: %s \n" % (self.__codigo,self.__sabor))

    def mostrarsabores(self):
        print("codigo : %s" %(self.__codigo))
        print("ingredientes : %s" %(self.__ingredientes))
        print("sabor : %s" %(self.__sabor))
        
    def getcodigo(self):
        return self.__codigo
    
    def __str__(self):
        return "\nCodigo:%s Ingredientes:%s Sabor:%s"%(self.__codigo,self.__ingredientes,self.__sabor)
