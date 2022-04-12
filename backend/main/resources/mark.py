from flask_restful import Resource
from flask import request

MARKS = {
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

class Mark(Resource):

    def get(self, id):
        if int(id) in MARKS:
            return MARKS[int(id)]
        return '', 404

    def delete(self, id):
        if int(id) in MARKS:
            del MARKS[int(id)]
            return '', 204
        return '', 404


class Marks(Resource):
    def get(self):
        return MARKS

    def post(self):
        Marks = request.get_json()
        id = int(max(MARKS.keys())) + 1
        MARKS[id] = Poemas
        return MARKS[id], 201