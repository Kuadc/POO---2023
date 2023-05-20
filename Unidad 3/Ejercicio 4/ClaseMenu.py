

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.opcion4,
                            '5':self.salir
                          }

    def opcion(self,op,arreglo):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='2' or op=='3' or op=='4':
            func(arreglo)
        else:
            func()
    def opcion1(self,arreglo):
        ''' 1. Registrar horas: Ingresar el DNI de un empleado y la cantidad de horas trabajadas en el día de la fecha
        e incrementar la cantidad de las horas trabajadas del empleado.'''
        d = input("Ingrese el DNI del empleado: ")
        h = int(input("Ingrese la cantidad de horas trabajadas: "))
        if isinstance(h,int) and isinstance(d,str):
            arreglo.Buscareincrementar(d,h)
        else:
            print("Se estan ingresando mal los valores")

    def opcion2(self,arreglo):
        """2. Total de tarea: Dada una tarea mostrar el monto a pagar para ella.
        Solo se consideran las tareas que no han finalizado."""
        ta = input("Igrese la tarea a consular: ")
        if isinstance(ta,str):
            arreglo.buscartarea(ta)
        return
    def opcion3(self, arreglo):
        """3. Ayuda Económica: La empresa dará una ayuda solidaria a los empleados cuyo sueldo sea inferior a $150000;
        listar nombre, dirección y DNI de los empleados que les corresponde la ayuda."""
        arreglo.ayudaeconomica()
        return
    def opcion4(self, arreglo):
        """4. Calcular sueldo: Mostrar nombre, teléfono y sueldo a cobrar de todos los empleados."""
        arreglo.calcularymostrarsueldo()
        return
    def salir(self):
        exit()
