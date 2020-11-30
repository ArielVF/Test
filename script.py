from datetime import datetime
import requests

#Obtenemos la url que tienen la incidencias
url = 'http://5fc1ea689210060016869270.mockapi.io/problems'

#se obtiene la fecha del dia actual
date = datetime.now().strftime('%Y/%m/%d %H:%M:%S')

#Se solicita titulo y descripcion al usuario
title = raw_input("Titulo: ")
description= raw_input('Descripcion: ')

#Si no hay un tamanio en el titulo y la descripcion no se inserta la nueva incidencia, puesto que se necesitan esos parametros
if len(title) > 0 and len(description) > 0:
    issue = {
            "Fecha": date,
            "Titulo": title,
            "Descripcion": description,
            "Agente": "Python script agente"
        }
    requests.post(url, issue)
    print ("Incidencia '"+title+"' agregada correctamente.")
else:
    print("Los campos Titulo y Descripcion deben contener algun parametro")
