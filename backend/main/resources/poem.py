from flask_restful import Resource
from flask import request


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

class Poem(Resource):

    def get(self, id):
        if int(id) in POEMS:
            return POEMS[int(id)]
        return '', 404

    def delete(self, id):
        if int(id) in POEMS:
            del POEMS[int(id)]
            return '', 204
        return '', 404


class Poems(Resource):

    def get(self):
        return POEMS

    def post(self):
        Poems = request.get_json()
        id = int(max(POEMS.keys())) + 1
        POEMS[id] = Poems
        return POEMS[id], 201