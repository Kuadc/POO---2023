
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
