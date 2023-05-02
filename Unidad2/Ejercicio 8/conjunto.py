

class ClaseConjunto:
    __unconjunto = []
    
    def __init__(self):
        self.__unconjunto = []
        
    def Agregarelementos(self):
        print("*** Ahora agregaremos elementos al conjunto ***")
        numero = int(input("Ingrese un numero, termine con 0: "))
        while numero != 0:
            self.__unconjunto.append(numero)
            numero = int(input("Ingrese un numero, termine con 0: "))    
        
    def __add__(self, B):
        conjunto = []
        self.__unconjunto.sort()
        B.__unconjunto.sort()
        a = len(self.__unconjunto)
        b = len(B.__unconjunto)
        i = 0
        j = 0
        while i<a and j<b:
            if self.__unconjunto[i] < B.__unconjunto[j]:
                conjunto.append(self.__unconjunto[i])
                #si es menor agrega
                i = i+1
            elif self.__unconjunto[i] == B.__unconjunto[j]:
                conjunto.append(self.__unconjunto[j])
                i = i+1
                j = j+1
                #si es igual agrega por una sola vez
            else: 
                conjunto.append(self.__unconjunto[i])
                i = i+1
                j = j+1
                #si es diferente agrega
        if i<a:
            while i<a:
                conjunto.append(self.__unconjunto[i])
                i+=1
                #si agrego todos los elementos del primer conjunto no pasa por aqui
        if j<b:
            while j<b:
                conjunto.append(B.__unconjunto[j])
                j+=1                
                #si agrego todos los elementos del segundo conjunto no pasa por aqui
                
        return conjunto
        
                    
    def __sub__(self, otro):
        conjunto = []
        self.__unconjunto.sort()
        otro.__unconjunto.sort()
        a = len(self.__unconjunto)
        b = len(otro.__unconjunto)
        i = 0
        j = 0
        band = False
        while i<a:
            band = False
            while j<b and band == False: 
                if self.__unconjunto[i] == otro.__unconjunto[j]:
                    band = True
                else: j = j+1
            if band == False:
                conjunto.append(self.__unconjunto[i])
                i = i+1
                j =  0
            else:
                i = i+1
                j = 0
            
        return conjunto
    
    def __eq__(self, otro):
        self.__unconjunto.sort()
        otro.__unconjunto.sort()
        a = len(self.__unconjunto)
        b = len(otro.__unconjunto)
        band = None
        if a == b:
            i = 0
            band = True
            while i<a and band == True: 
                if self.__unconjunto[i] == otro.__unconjunto[i]:
                    i=i+1                        
                else: 
                    band = False
        else: 
            band = False
                                
        return band
        
            
    def __str__(self):
        return "%s" %(self.__unconjunto)
        