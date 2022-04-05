from flask_restful import Resource
from flask import Flask
'''
class Usuarios(Resource):

    def get(self, id):
        if int(id) in USUARIO:
            return USUARIO[int(id)]
        return '', 404
'''

#Diccionario de prueba

USUARIO = {
    1: {'firstname': 'Lucas', 'lastname': 'Galdame'},
    2: {'firsname': 'Matias', 'lastname': 'Vilches'}
}

'''
/poemas/                /poema/<id>
/calificaciones/        /calificacion/<id>
/usuarios/              /usuario/<id>
'''

#Recurso Poema
class Usuario(Resource):
    #Obtener recurso
    def get(self, id):
        #Verificar que exista un Poem con ese Id en diccionario
        if int(id) in USUARIO:
            #Devolver poem correspondiente
            return USUARIO[int(id)]
        #Devolver error 404 en caso que no exista
        return '', 404
    #Eliminar recurso
    def delete(self, id):
        #Verificar que exista un Poem con ese Id en diccionario
        if int(id) in USUARIO:
            #Eliminar POEM del diccionario
            del USUARIO[int(id)]
            return '', 204
        return '', 404
    #Modificar recurso
    def put(self, id):
        if int(id) in USUARIO:
            Usuario = USUARIO[int(id)]
            #Obtengo los datos de la solicitud
            data = request.get_json()
            Usuario.update(data)
            return Usuario, 201
        return '', 404

#Recurso Profesores
class Usuarios(Resource):
    #Obtener lista de recursos
    def get(self):
        return USUARIO
    #Insertar recurso
    def post(self):
        #Obtener datos de la solicitud
        Usuarios = request.get_json()
        id = int(max(USUARIO.keys())) + 1
        USUARIO[id] = Usuarios
        return USUARIO[id], 201