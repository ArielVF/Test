from datetime import datetime
import requests

url = 'http://5fc1ea689210060016869270.mockapi.io/problems'
date = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
title = raw_input("Titulo: ")
description= raw_input('Descripcion: ')

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
