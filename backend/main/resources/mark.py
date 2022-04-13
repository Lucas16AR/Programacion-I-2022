from flask_restful import Resource
from flask import jsonify, request
from .. import db
from main.models import MarkModel

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
        mark = db.session.query(MarkModel).get_or_404(id)
        return mark.to_json()

    def delete(self, id):
        mark = db.session.query(MarkModel).get_or_404(id)
        db.session.delete(mark)
        db.session.commit()
        return '', 201
        
    def put(self, id):
        mark = db.session.query(MarkModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(mark, key, value)
        db.session.add(mark)
        return mark.to_json(), 201

class Marks(Resource):
    def get(self):
        marks = db.session.query(MarkModel).all()
        return jsonify([mark.to_json() for mark in marks])

    def post(self):
        mark = MarkModel.from_json(request.get_json())
        db.session.add(mark)
        db.session.commit()
        return mark.to_json(), 201