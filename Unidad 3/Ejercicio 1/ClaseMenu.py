

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.salir
                          }

    def opcion(self,op,lista):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='2':
            func(lista)
        else:
            func()

    def opcion1(self,lista):
        '''Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y
        duración de cada una de las carreras que se dictan en esa facultad.'''
        cod = int(input("Ingrese codigo de la facultad a consultar: "))
        if isinstance(cod,int):
            lista.mostrarfacultad(cod)



    def opcion2(self,lista):
        '''Ingrese el nombre de carrera, muestre el codigo(codigo de facultad y carrera), nombre y localidad de la facultad'''
        nombre = str(input("Ingrese nombre de la carrera: "))
        if isinstance(nombre,str):
            lista.mostrarcodigo(nombre)

    def salir(self):
        exit()
