from Plan import PlanAhorro

import csv

class lista:
    __lista = []
    
    def __init__(self):
        self.__lista = []
        
    def agregarregisrto(self,plan):
        self.__lista.append(plan)
        
    def cargararchivo(self):
        archivo = open("archivo.csv")
        reader = csv.reader(archivo,delimiter=";")
        fila = next(reader)
        bandera = fila[4]
        archivo.seek(0)
        for fila in reader:
            codigo = int(fila[0])
            modelo = fila[1]
            version = fila[2]
            valor = int(fila[3])
            cantcuotas = int(fila[4])
            cantlicitar = int(fila[5])
            if bandera != cantcuotas:
                PlanAhorro.cantidadcuotasplan=cantcuotas
                PlanAhorro.cantidadcuotaslicitar = cantlicitar
                bandera = cantcuotas
                unplan = PlanAhorro(codigo,modelo,version,valor)
                self.agregarregisrto(unplan)                
            else:
                unplan = PlanAhorro(codigo,modelo,version,valor)
                self.agregarregisrto(unplan)                
        archivo.close()
        
    def ModificarValor(self):
        for plan in self.__lista:
            print(plan)
            valor = int(input("Ingrese nuevo valor del vehiculo: "))
            plan.ModificarValorVehiculo(valor)
            
    def BuscarCuotaInferior(self,valor):
        for plan in (self.__lista):
            #valor cuota = (importe vehículo/cantidad de cuotas) + importe vehículo * 0.1
            importe = plan.GetValor()
            cant = PlanAhorro.getcantcuotas()
            valorCuota = (importe/cant) + importe * 0.1
            if valorCuota <valor:
                plan.mostrarDatos()
    
    def BuscarMontoLicitacion(self):
        for plan in self.__lista:
            print(plan)
            importe = plan.GetValor()
            cant = PlanAhorro.getcantcuotas()
            valorCuota = (importe/cant) + importe * 0.1
            # (cantidad de cuotas para licitar * importe de la cuota)
            cant2 = PlanAhorro.getcantcuotaslicitar()
            montoparaLicitar = cant2 * valorCuota
            print ("El monto para Licitar Este Vehiculo es de :{:.2f} \n".format(montoparaLicitar))

                                   
    def __str__(self):
         s = ""
         for libro in self.__lista:
             s += str(libro) + '\n'
         return s
