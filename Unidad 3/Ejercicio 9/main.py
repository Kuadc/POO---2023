from ClaseLista import Lista

from ClaseObjectEncoder import ObjectEncoder

from ClaseVehiculoNuevo import VehiculoNuevo

from ClaseVehiculoUsado import VehiculoUsado

import unittest
class TestVehiculos(unittest.TestCase):
    def setUp(self):
        jsonF = ObjectEncoder()
        diccionario = jsonF.leerJSONArchivo('Vehiculos.json')
        self.__lista = jsonF.decodificarDiccionario(diccionario)

    def test_insertarvehiculo_pos0(self):
        elemento = VehiculoNuevo("punto","5","rojo",1000,"fiat","base")
        pos = 0
        self.__lista.InsertarElemento(elemento,pos)
        self.assertEqual(self.__lista.getTope(),5)

    def test_insertarvehiculo_pos2(self):
        elemento = VehiculoNuevo("mobi", "3", "verde", 3000, "fiat", "full")
        pos = 2
        self.__lista.InsertarElemento(elemento, pos)
        self.assertEqual(self.__lista.getTope(), 5)

    def test_insertarvehiculo_posultima(self):
        elemento = VehiculoNuevo("argo", "5", "azul", 5000, "fiat", "base")
        pos = self.__lista.getTope()
        self.__lista.InsertarElemento(elemento, pos)
        self.assertEqual(self.__lista.getTope(), 5)

    def test_agregarelemento(self):
        elemento = VehiculoNuevo("argo", "5", "azul", 5000, "fiat", "base")
        self.__lista.AgregarElemento(elemento)
        self.assertEqual(self.__lista.getTope(), 5)

    def test_verificarobjeto(self):
        pos = 2
        objeto= self.__lista.MostrarElemento(pos)
        self.assertEqual(objeto,VehiculoUsado)

    def test_modificarpreciobase(self):
        vehiculo=self.__lista.BuscarMarca("UGD453")
        self.assertEqual(vehiculo.getpreciobase(),5400)

if __name__ == '__main__':
    unittest.main()
