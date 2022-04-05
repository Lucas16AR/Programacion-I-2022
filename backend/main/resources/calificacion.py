from flask_restful import Resource
from flask import Flask

#Diccionario de prueba

CALIFICACION = {
    1: {'calificacion': 8.1},
    2: {'calificacion': 10},
    3: {'calificacion': 9.1},
    4: {'calificacion': 5.6},
    5: {'calificacion': 6.7}
}

'''
/poemas/                /poema/<id>
/calificaciones/        /calificacion/<id>
/usuarios/              /usuario/<id>
'''

#Recurso Poema
class Calificacion(Resource):
    #Obtener recurso
    def get(self, id):
        #Verificar que exista un Poem con ese Id en diccionario
        if int(id) in CALIFICACION:
            #Devolver poem correspondiente
            return CALIFICACION[int(id)]
        #Devolver error 404 en caso que no exista
        return '', 404
    #Eliminar recurso
    def delete(self, id):
        #Verificar que exista un Poem con ese Id en diccionario
        if int(id) in CALIFICACION:
            #Eliminar POEM del diccionario
            del CALIFICACION[int(id)]
            return '', 204
        return '', 404
    #Modificar recurso
    def put(self, id):
        if int(id) in CALIFICACION:
            Calificacion = CALIFICACION[int(id)]
            #Obtengo los datos de la solicitud
            data = request.get_json()
            Calificacion.update(data)
            return Calificacion, 201
        return '', 404

#Recurso Profesores
class Calificaciones(Resource):
    #Obtener lista de recursos
    def get(self):
        return CALIFICACION
    #Insertar recurso
    def post(self):
        #Obtener datos de la solicitud
        Calificaciones = request.get_json()
        id = int(max(CALIFICACION.keys())) + 1
        CALIFICACION[id] = Poemas
        return CALIFICACION[id], 201