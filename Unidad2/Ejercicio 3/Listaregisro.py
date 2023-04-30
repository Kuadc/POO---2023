from Registro import registro
import csv

class lista:
    __lista = []
    
    def __init__(self):
        self.__lista = []
        
    def agregarregisrto(self,registro,dia,hora):
        self.__lista[dia-1][hora-1] = registro
        

        
        
    def cargararchivo(self):
        self.__lista =[[ 0 for colum in range(24)]for fila in range(2)]
        archivo = open("archivo.csv")
        reader = csv.reader(archivo,delimiter=";")
        for fila in reader:
            dia = int(fila[0])
            hora = int(fila[1])
            temp = int(fila[2])
            hum = int(fila[3])
            pres = int(fila[4])
            unregistro = registro(temp,hum,pres)
            self.agregarregisrto(unregistro,dia,hora)
        archivo.close()
        
    def mostrarmayortemp(self):
        max=0
        min=999
        for i in range(len(self.__lista)): #cantidad de filas
            for j in range(len(self.__lista[i])): #cantidad de columnas por fila
                #print("temperatura %s" %(self.__lista[i][j].Gettemp()) )#
                if max < self.__lista[i][j].Gettemp():
                    max = self.__lista[i][j].Gettemp()
                    dia = i+1
                    hora = j
                if min > self.__lista[i][j].Gettemp():
                    min = self.__lista[i][j].Gettemp()
                    dia1 = i+1
                    hora1 = j
        print("El dia : {} y la hora: {} de mayor temperatura fue de : {}" .format(dia,hora,max))
        print("El dia : {} y la hora: {} de menor temperatura fue de : {}" .format(dia1,hora1,min))
        return
    
    def mostrarmayorhumedad(self):
        max=0
        min=999
        for i in range(len(self.__lista)): #cantidad de filas
            for j in range(len(self.__lista[i])): #cantidad de columnas por fila
                #print("temperatura %s" %(self.__lista[i][j].Gettemp()) )#
                if max < self.__lista[i][j].Gethumedad():
                    max = self.__lista[i][j].Gethumedad()
                    dia = i+1
                    hora = j
                if min > self.__lista[i][j].Gethumedad():
                    min = self.__lista[i][j].Gethumedad()
                    dia1 = i+1
                    hora1 = j
        print("El dia : {} y la hora: {} , de mayor humedad fue de : {}" .format(dia,hora,max))
        print("El dia : {} y la hora: {} , de menor humedad fue de : {}" .format(dia1,hora1,min))
        return
    
    def mostrarmayorpresion(self):
        max=0
        min=999
        for i in range(len(self.__lista)): #cantidad de filas
            for j in range(len(self.__lista[i])): #cantidad de columnas por fila
                #print("temperatura %s" %(self.__lista[i][j].Gettemp()) )#
                if max < self.__lista[i][j].Getpresion():
                    max = self.__lista[i][j].Getpresion()
                    dia = i+1
                    hora = j
                if min > self.__lista[i][j].Getpresion():
                    min = self.__lista[i][j].Getpresion()
                    dia1 = i+1
                    hora1 = j
        print("El dia : {} y la hora: {} , de mayor humedad fue de : {}" .format(dia,hora,max))
        print("El dia : {} y la hora: {} , de menor humedad fue de : {}" .format(dia1,hora1,min))
        return
    
    def promediomensual(self):
        i = 0
        while i < len(self.__lista[0]):
            j= 0
            acum=0
            while j < len(self.__lista):
                acum = self.__lista[j][i].Gettemp() + acum
                j = j+1
            promedio = acum/2
            print("Para la hora {} el promedio mensual de la temperatura es de {}".format(i+1, promedio))
            i=i+1
        #for i in range(len(self.__lista[0])):
         #   for j in range(len(self.__lista)):
          #      acum = self.__lista[j][i].Gettemp() + acum
           # promedio = acum/2
            #print("Para la hora {} el promedio mensual de la temperatura es de {}".format(i+1, promedio))
        #for i in range(24): #cantidad de filas
         #   for j in range(2): #cantidad de columnas por fila
          #      acum = self.__lista[j][i].Gettemp() + acum
           # promedio = acum/2
            #print("Para la hora {} el promedio mensual de la temperatura es de {}".format(i+1, promedio))
        return
    
    def mostrarvariables(self,dia):
        H = "Hora"
        t ="Temperatura"
        hu = "Humedad"
        p = "Presion"
        #print("{:^15}{:^15}{:^15}{:^15}".format(H,t,hu,p))
        print(f"{H:^15}{t:^15}{hu:^15}{p:^15}")#desde python 3.6 y superior colocando la "f"
        for i in range(24):
            print("{:^15}{:^15}{:^15}{:^15}" .format(i,self.__lista[dia][i].Gettemp(),self.__lista[dia-1][i].Gethumedad(),self.__lista[dia][i].Getpresion()))
    
    """def mostrarmenortemp(self):
         min=999
         for i in range(len(self.__lista)): #cantidad de filas
             for j in range(len(self.__lista[i])): #cantidad de columnas por fila
                 #print("temperatura %s" %(self.__lista[i][j].Gettemp()) )#
                 
         print("El dia : {} y la hora: {} , la menor temp fue de : {}" .format(dia,hora,min))"""
        
    def __str__(self):
         s=""
         for fila in self.__lista:
             for columna in fila:
                s += str(columna) + '\n'
         return s