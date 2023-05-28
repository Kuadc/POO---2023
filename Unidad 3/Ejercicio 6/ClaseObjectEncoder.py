import json
from pathlib import Path

from ClaseLista import Lista

from ClaseVehiculoNuevo import VehiculoNuevo

from ClaseVehiculoUsado import VehiculoUsado
class ObjectEncoder(object):
    def decodificarDiccionario(self, d):
        if '__class__' not in d: #si la la clave "__class__" no esa presente en el diccionario (por lo tanto no se puede decodificar el diccionario porque no contiene información sobre la clase)
         return d
        else:
            class_name=d['__class__'] # en contenido de la clave "__class__" del diccionario "d" se asigna a class_name
            class_=eval(class_name) # se utiliza la funcion eval, para evaluar el nombre de la clase y obtener la referencia a la clase, se asigna a a la variable.
            if class_name=='Lista': #si la el nombre de la clase es igual a el manejador "lista". se decodifica el contenido
                vehiculo=d['Vehiculo'] # el cotenido de la clave "vehiculo" se asigna a vehiculo
                unvehiculo = vehiculo[0] # se obtiene el primer elementto de la lista puntos y se guarda en "dpunto"
                manejadorlista=class_()  # se crea una instancia con el nombre manejador ( que es una lista)
                for i in range(len(vehiculo)):
                    unvehiculo = vehiculo[i] #el primer elemento de la lista puntos que contiene los objetos/instancia de la clase punto
                    class_name = unvehiculo.pop('__class__') #se obtiene el nobre de la clase utilziando "pop", que elimina y obtiene el valor de la clavwe "__class__"
                    class_ = eval(class_name) #evalua nuevamente el bnombre de la clase y se guiarda en class_
                    atributos = unvehiculo['__atributos__'] #se obtiene todos los atributos que tiene el objeto punto y se guarda como  un dicionaro
                    unveh= class_(**atributos) #se crea una instancia de la clase punto (en este caso) y se le pasan por parametos los atributos.
                    manejadorlista.AgregarElemento(unveh) # se agregar los puntos a la lista.
                return manejadorlista

    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()

    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario

    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)
