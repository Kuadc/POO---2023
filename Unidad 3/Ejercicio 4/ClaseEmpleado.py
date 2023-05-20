
class Empleado:
    __dni = ""
    __nombre = ""
    __direccion = ""
    __telefono = ""

    def __init__(self, **kwargs):
        self.__dni = kwargs['dni']
        self.__nombre = kwargs['nombre']
        self.__direccion = kwargs['direccion']
        self.__telefono = kwargs['telefono']

    def getdni(self):
        return self.__dni

    def getnombre(self):
        return self.__nombre

    def getdireccion(self):
        return self.__direccion

    def gettelefono(self):
        return self.__telefono

    def calcularsueldo(self):
        pass

    def listarempleado(self):
        print("DNI: {}\n Nombre:{}\n Direccion:{}\n".format(self.__dni,self.__nombre,self.__direccion))

    def mostrarnomytel(self):
        print("\nNombre:{}\nTelefono:{}".format(self.__nombre,self.__telefono))
