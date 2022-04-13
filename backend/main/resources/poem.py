from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import PoemModel


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
        poem = db.session.query(PoemModel).get_or_404(id)
        return poem.to_json()

    def delete(self, id):
        poem = db.session.query(PoemModel).get_or_404()
        db.session.delete(poem)
        db.session.commit()
        return '', 204

    def put (self, id):
        poem = db.session.query(PoemModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(poem, key, value)
        db.session.add(poem)
        db.session.commit()
        return poem.to_json(), 201 

class Poems(Resource):

    def get(self):
        poems = db.session.query(PoemModel).get_or_404(id)
        return jsonify([poem.to_json() for poem in poems])

    def post(self):
        poem = PoemModel.from_json(request.get_json())
        db.session.add(poem)
        db.session.commit()
        return poem.to_json(), 201