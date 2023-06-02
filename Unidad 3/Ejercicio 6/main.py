from ClaseLista import Lista

from ClaseObjectEncoder import ObjectEncoder

from ClaseVehiculoNuevo import VehiculoNuevo

from ClaseVehiculoUsado import VehiculoUsado

if __name__ == '__main__':
    jsonF = ObjectEncoder()
    diccionario = jsonF.leerJSONArchivo('Vehiculos.json')
    lista = jsonF.decodificarDiccionario(diccionario)
    bandera = True
    while bandera:
        print("1 - Insertar un vehículo en la colección en una posición determinada.")
        print("2 - Agregar un vehículo a la colección.")
        print("3 - Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.")
        print("4 - Dada la patente de un vehículo usado, modificar el precio base, y luego mostrar el precio de venta.")
        print("5 - Mostrar todos los datos, incluido el importe de venta, del vehículo más económico.")
        print("6 - Mostrar para todos los vehículos que la concesionaria tiene a la venta, modelo, cantidad de puertas e importe de venta.")
        print("7 - Almacenar los objetos de la colección Lista en el archivo “Vehiculos.json”.")
        print("8 -  Salir")
        opcion = int(input("Elija una opcion: "))
        if opcion == 1:
                atributos = {
                    "modelo": "falcon",
                    "puertas": 5,
                    "color": "verde",
                    "preciobase": 2500,
                    "marca": "ford",
                    "patente": "UGD453",
                    "anio": 1985,
                    "kilometraje": 250
                }
                unvehiculo = VehiculoUsado(**atributos)
                print(unvehiculo)
                pos = int(input("Igrese la posicion donde desea agregar el nuevo vehiculo: "))
                try:
                    lista.InsertarElemento(unvehiculo, pos)
                except IndexError:
                    print("\n !Cuidado! - La posicion del elemento no es valida\n")

        elif opcion == 2:
                print("Que tipo de vehiculo desea agregar")
                print("1 - Vehiculo Usado")
                print("2 - Vehiculo Nuevo")
                op = int(input("Ingrese la opcion deseada"))
                if op ==1:
                    atributos = {
                        "modelo": "Fiesta",
                        "puertas": 3,
                        "color": "Azul Marino",
                        "preciobase": 5500,
                        "marca": "Ford",
                        "patente": "JKI453",
                        "anio": 1999,
                        "kilometraje": 100
                    }
                    unvehiculo = VehiculoUsado(**atributos)
                    print("El siguiente vehiculo sera agregado")
                    print(unvehiculo)
                    lista.AgregarElemento(unvehiculo)
                else:
                    atributos = {
                        "modelo": "Canguro",
                        "puertas": 3,
                        "color": "Morado",
                        "preciobase": 95000,
                        "marca": "Toyota",
                        "version":"full"
                    }
                    unvehiculo = VehiculoNuevo(**atributos)
                    print("El siguiente vehiculo sera agregado")
                    print(unvehiculo)
                    lista.AgregarElemento(unvehiculo)

        elif opcion == 3:
                pos = int(input("Igrese la posicion del vehiculo que desea ver: "))
                try:
                    lista.MostrarElemento(pos)
                except IndexError:
                    print("\nLa posicion enviada no es correcta o no existe el elemento alguno en esa posicion\n")
        elif opcion == 4:
                patente = input("Ingrese la patenet del Vehiculo Usado")
                lista.BuscarMarca(patente)
        elif opcion == 5:
                lista.buscareconomico()
        elif opcion == 6:
                for dato in lista:
                    print(dato)
                    dato.importeventa()
        elif opcion == 7:
            d = lista.toJSON()
            jsonF.guardarJSONArchivo(d, 'Vehiculos.json')
        else :
            bandera = False
            print("____Usted finalizo el programa____")
