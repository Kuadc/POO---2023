import json
from pathlib import Path

from ClaseLista import Lista

from ClaseDocente  import Docente
from ClaseInvestigador import Investigador
from ClaseDocenteInvestigador import DocenteInvestigador
from ClaseApoyo import Apoyo
from ClasePersonal import Personal

class ObjectEncoder(object):
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
         return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Lista':
                agente=d['Personal']
                unagente = agente[0]
                manejadorlista=class_()
                for i in range(len(agente)):
                    unagente = agente[i]
                    class_name = unagente.pop('__class__')
                    class_ = eval(class_name)
                    atributos = unagente['__atributos__']
                    unagent= class_(**atributos)
                    manejadorlista.AgregarElemento(unagent)
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
