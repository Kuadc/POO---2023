import json
from pathlib import Path

from ClaseLista import Lista

from ClaseVehiculoNuevo import VehiculoNuevo

from ClaseVehiculoUsado import VehiculoUsado
class ObjectEncoder(object):
    def decodificarDiccionario(self, d):
        if '__class__' not in d: 
         return d
        else:
            class_name=d['__class__']
            class_=eval(class_name) 
            if class_name=='Lista': 
                vehiculo=d['Vehiculo']
                unvehiculo = vehiculo[0] 
                manejadorlista=class_()  
                for i in range(len(vehiculo)):
                    unvehiculo = vehiculo[i] 
                    class_name = unvehiculo.pop('__class__') 
                    class_ = eval(class_name) 
                    atributos = unvehiculo['__atributos__'] 
                    unveh= class_(**atributos) 
                    manejadorlista.AgregarElemento(unveh)
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
