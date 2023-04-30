from Viajero import viajeroFrecuente
import csv

class lista:
    __lista = []
    
    def __init__(self):
        self.__lista = []
        
    def agregarviajero(self,viajero):
        self.__lista.append(viajero)
    
    def cantidadMillas(self):
        i = 0
        mayor = self.__lista[i]
        while i < len(self.__lista):
            if self.__lista[i] > mayor:
                mayor = self.__lista[i]
                i = i+1
            else: i = i+1
        return mayor.cantidadTotaldeMillas()         
    
    def buscarViajeros(self, millas):
        print("Viajero/s con mayor cantidad de millas\n")
        i = 0
        while i < len(self.__lista):
            if millas == self.__lista[i].cantidadTotaldeMillas():
                print(self.__lista[i])
                i = i+1
            else: i= i+1
            
    def AcumularMillas(self,num,millas):
        i=0
        band = False
        while (i < len(self.__lista)) & (band == False):
            if num == self.__lista[i].Getnumviajero():
                viajero = self.__lista[i] + millas
                i = i+1
            else: 
                i = i+1
        print("\n Nueva instancia de la clase viajero")
        print(viajero)
        
    def restarMillas(self,num,millas):        
            i=0
            band = False
            while (i < len(self.__lista)) & (band == False):
                if num == self.__lista[i].Getnumviajero():
                    viajero = self.__lista[i] - millas
                    band = True
                    i = i+1
                else: 
                    i = i+1
            print("\n Nueva instancia de la clase viajero")
            print(viajero)
    
    def compararmillas(self,millas):
        i = 0
        while i < len(self.__lista):
            if millas == self.__lista[i]:
                print("Millas iguales")
                i = i+1
            else:
                i = i+1
                
    def AcumularMillasPorDerecha(self, num, millas):
        i=0
        band = False
        while (i < len(self.__lista)) & (band == False):
            if num == self.__lista[i].Getnumviajero():
                viajero = millas + self.__lista[i]
                i = i+1
            else: 
                i = i+1
        print("\n Nueva instancia de la clase viajero")
        print(viajero)
        
    def CanjearMillasPorDerecha(self, num, millas):
            i=0
            band = False
            while (i < len(self.__lista)) & (band == False):
                if num == self.__lista[i].Getnumviajero():
                    viajero = millas - self.__lista[i]
                    band = True
                    i = i+1
                else: 
                    i = i+1
            print("\n Nueva instancia de la clase viajero")
            print(viajero)
        
        
    def cargararchivo(self):
        archivo = open("viajeros.csv")
        reader = csv.reader(archivo,delimiter=";")
        bandera = True
        for fila in reader:
            if bandera:
                #saltear titulo
                bandera = False
            else:
                viajero = int(fila[0])
                dni = int(fila[1])
                nombre = fila[2]
                apellido = fila[3]
                millas = int(fila[4])
                unviajero = viajeroFrecuente(viajero,dni,nombre,apellido,millas)
                self.agregarviajero(unviajero)
        archivo.close()
        
    
    def __str__(self):
        s = ""
        
        for fila in self.__lista:
            s+=str(fila) + "\n \n" 
        return s
    
                
