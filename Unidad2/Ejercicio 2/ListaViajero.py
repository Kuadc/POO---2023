from Viajero import viajeroFrecuente
import csv

class lista:
    __lista = []
    
    def __init__(self):
        self.__lista = []
        
    def agregarviajero(self,viajero):
        self.__lista.append(viajero)
        
    def buscarviajero(self,numviajero):
        for indice, viajero in enumerate(self.__lista):
            if viajero.Getnumviajero() == numviajero:
                return indice
        
        
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
        
    def cambiarMillas(self, indice):
        totalmillas= self.__lista[indice].cantidadTotaldeMillas()
        return totalmillas
        
    def acumular_millas(self,indice,millas):
        totalacumulado= self.__lista[indice].acumularMillas(millas)
        return totalacumulado
    
    def canjearMillas(self,indice,millas):
        totalcanjeado = self.__lista[indice].canjearMillas(millas)
        return totalcanjeado
    
                
