#Se importan librerias y dependencias
from flask import Flask, jsonify, request, json, make_response
import requests, jwt, datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'
token = ''

#url donde estan los datos
url1 = 'http://5fc1ea689210060016869270.mockapi.io/problems'
url2 = 'http://5fc1ea689210060016869270.mockapi.io/agent'

#Agrega agente
@app.route('/agent', methods=['POST'])
def addAgent():
    newAgent = {
        "nombre": request.json['nombre'],
        "clave": request.json['clave']
    }
    requests.post(url2, newAgent)
    return "Agente "+request.json['nombre']+" agregado satisfactoriamente"

#Permite crear incidencia si un agente esta registrado
@app.route('/issue', methods=['POST'])
def issue():
    if 'access-token' in request.headers: #Se valida el token agregado por el usuario
        aux_token = request.headers['access-token']
        if aux_token == token and token != '': #Se comparan los token, en caso de coincidir el usuario puede insertar una incidencia
            newIssue = {
                "Fecha": request.json['Fecha'],
                "Titulo": request.json['Titulo'],
                "Descripcion": request.json['Descripcion'],
                "Agente": current_user
            }
            requests.post(url1, newIssue)
            return 'Incidencia "'+request.json['Titulo']+'" agregada correctamente'
        else:
            return jsonify({'Alerta': 'El token no es valido, no puede acceder a estar ruta'}), 401
    else:
        return jsonify({'Alerta': 'No existe un token de autentificacion'}), 401

#autentificacion
@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password: #Valida si el usuario no ha iniciado un apartado de authorization en postman
        return make_response('No se ha autentificado', 401, {'WWW-Autheticate': 'Basic realm="Login Required!"'})
    else:
        response = requests.get(url2)
        users = response.json()
        for user in users:
            if user['nombre'] == auth.username and user['clave'] == auth.password:
                global token, current_user
                current_user = auth.username
                token = jwt.encode({'username': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15)}, app.config['SECRET_KEY'])
                return jsonify({'token': token.decode('UTF-8')})
        return make_response('Usuario no valido', 401, {'WWW-Autheticate': 'Basic realm="Login Required!"'})

#Obtiene las incidencias
@app.route('/issues', methods=['GET'])
def returnIssues():
    response = requests.get(url1)
    problems = response.json()
    return jsonify(problems)

#filtra incidencias por agente
@app.route('/issues/<string:name_agent>')
def searchIssuesAgent(name_agent):
    response = requests.get(url1)
    problems = response.json()
    issuesAgent = [problem for problem in problems if problem['Agente'] == name_agent]
    return jsonify(issuesAgent)

#filtrar por fecha
@app.route('/issues/<int:date_issues>')
def searchIssuesDate(date_issues):
    response = requests.get(url1)
    problems = response.json()
    results = []
    for problem in problems:
        date = problem['Fecha'].split(" ")
        date_aux = date[0].split("/")
        final_date = date_aux[0]+date_aux[1]+date_aux[2]
        if date_issues == int(final_date):
            results += [problem]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug = True, port = 4000)
