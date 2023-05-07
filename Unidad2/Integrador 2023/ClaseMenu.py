
class Menu:
    __switcher = {}

    def __init__(self):
        self.__switcher = {"1":self.opcion1,"2":self.opcion2,"3":self.opcion3,"4":self.salir}

    def opcionmenu(self,op,lista,arreglo):
        funcion = self.__switcher.get(op,lambda : print("opcion no valida"))
        if op == "1" or op == "2" or op=="3":
            funcion(lista,arreglo)
        else:
            funcion()

    def opcion1(self,lista,arreglo):
        """"
        Leer por teclado el número de dni de un alumno, e informar su promedio con
        aplazos y sin aplazos."""

        dni = input("Ingrese el dni del alumno: ")
        lista.BuscarAlumno(dni)
        return

    def opcion2(self,lista,arreglo):
        """Leer por teclado el nombre de una materia, e informar los estudiantes que la
        aprobaron en forma promocional, con nota mayor o igual que 7.
        con el siguiente formato: DNI - Apellido y nombre - Fecha - Nota - Año que cursa"""
        materia = input("Ingrese el nombre de la materia a consultar: ")
        lista.BuscarMateria(arreglo,materia)
        return

    def opcion3(self,lista,arreglo):
        """Obtener un listado de alumnos ordenado: por el año que cursan y alfabéticamente
        por apellido y nombre (ambos de menor a mayor). """
        arreglo.Ordenar()
        arreglo.mostrardatos()
        return

    def salir(self):
        exit()
        return
