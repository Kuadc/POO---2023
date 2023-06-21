

from ClaseObjectEncoder import ObjectEncoder

from vistaContactos import ContactsView
import json
from claseControladorContactos import ControladorContactos
import requests



if __name__ == "__main__":

    jsonFgeneros = ObjectEncoder()
    diccionario = jsonFgeneros.leerJSONArchivo('generos.json')
    listagenero = jsonFgeneros.decodificargeneros(diccionario)

    jsonF = ObjectEncoder()
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=5d05d8c832406f737ca16767ca765638'
    response = requests.get(url)
    if response.status_code == 200:
        # La solicitud fue exitosa
        data = response.json()  # Obtén los datos de respuesta en formato JSON
        # Trabaja con los datos recibidos
    else:
        # La solicitud falló
        print('Error:', response.status_code)

    listapeli = jsonF.decodificarpeliculas(data,listagenero)
    #print(listapeli)
    vista = ContactsView()
    ctrl = ControladorContactos(listapeli, vista)
    vista.setControlador(ctrl)
    ctrl.start()
