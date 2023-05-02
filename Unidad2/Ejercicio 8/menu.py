

class Menu:
    __menu =None
    def __init__(self):
        self.__menu = {'1': self.opcion1,
                       '2': self.opcion2,
                       '3': self.opcion3,
                       '4': self.salir}
    
    def opcion(self, op, A, B):
        funcion = self.__menu.get(op, lambda: print("opcion no valida"))
        if op == '1' or op=='2' or op=='3' :
            funcion(A, B)
        else:
            funcion()
    
    def opcion1(self,A,B):
        """La unión de dos conjuntos, para ello sobrecargue el operador binario suma (+). 
        Teniendo en cuenta que la unión es un nuevo conjunto que posee los elementos de ambos conjuntos, 
        en caso de haber elementos repetidos solo aparecen una vez en el resultado."""
        C = A+B
        print("\n Nuevo conjunto : ",C)
        return
    
    def opcion2(self,A,B):
        """La diferencia de dos conjuntos, para ello sobrecargue el operador binario resta (-). 
        Teniendo en cuenta que el resultado de la diferencia de conjuntos es un nuevo conjunto 
        que posee los elementos del primer operando que no se encuentren en el segundo operando"""
        C = A-B
        print("\n Nuevo conjunto : ",C)
        return
    
    def opcion3(self,A,B): 
        """Verificar si dos conjuntos son iguales, para ello sobrecargue el operador “==” 
        teniendo en cuenta que dos conjuntos se consideran iguales si tienen la misma 
        cantidad de elementos y sus valores son iguales (sin importar el orden de los elementos)"""
        if A == B: 
            print("\n***___Son iguales___***\n")
        else: 
            print("\n______No son iguales_____\n")
        return
    
    def salir(self):
        return
            