from flask_restful import Resource
from flask import Flask
'''
class Poema(Resource):

    def get(self, id):
        if int(id) in POEMS:
            return POEMS[int(id)]
        return '', 404
'''

#Diccionario de prueba

POEMS = {
    1: {'poemas': 'el lirico'},
    2: {'poemas': 'yo creo'},
    3: {'poemas': 'listo'},
    4: {'poemas': 'reus'},
    5: {'poemas': 'elpa'}
}

'''
/poemas/                /poema/<id>
/calificaciones/        /calificacion/<id>
/usuarios/              /usuario/<id>
'''

#Recurso Poema
class Poema(Resource):
    #Obtener recurso
    def get(self, id):
        #Verificar que exista un Poem con ese Id en diccionario
        if int(id) in POEMS:
            #Devolver poem correspondiente
            return POEMS[int(id)]
        #Devolver error 404 en caso que no exista
        return '', 404
    #Eliminar recurso
    def delete(self, id):
        #Verificar que exista un Poema   con ese Id en diccionario
        if int(id) in POEMS:
            #Eliminar POEM del diccionario
            del POEMS[int(id)]
            return '', 204 #Devolver poema correspondiente
            return Poema[int(id)]
        #Devolver error 404 en caso que no exista
        return '', 404
    #Eliminar recurso
    def delete(self, id):
        #Verificar que exista un Poem con ese Id en diccionario
        if int(id) in POEMS:
            #Eliminar POEM del diccionario
            del POEMS[int(id)]
            return '', 204
        return '', 404
    #Modificar recurso
    def put(self, id):
        if int(id) in POEMS:
            Poema = POEMS[int(id)]
            #Obtengo los datos de la solicitud
            data = request.get_json()
            Poema.update(data)
            return Poema, 201
        return '', 404

#Recurso Profesores
class Poemas(Resource):
    #Obtener lista de recursos
    def get(self):
        return POEMS
    #Insertar recurso
    def post(self):
        #Obtener datos de la solicitud
        Poemas = request.get_json()
        id = int(max(POEMS.keys())) + 1
        POEMS[id] = Poemas
        return POEMS[id], 201
        return '', 404
    #Modificar recurso
    def put(self, id):
        if int(id) in POEMS:
            Poema = POEMS[int(id)]
            #Obtengo los datos de la solicitud
            data = request.get_json()
            Poema.update(data)
            return Poema, 201
        return '', 404

#Recurso Profesores
class Poemas(Resource):
    #Obtener lista de recursos
    def get(self):
        return POEMS
    #Insertar recurso
    def post(self):
        #Obtener datos de la solicitud
        Poemas = request.get_json()
        id = int(max(POEMS.keys())) + 1
        POEMS[id] = Poemas
        return POEMS[id], 201