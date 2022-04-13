from flask_restful import Resource
from flask import jsonify, request
from .. import db
from main.models import UserModel

USERS = {
    1: {'firstname': 'Lucas', 'lastname': 'Galdame'},
    2: {'firsname': 'Matias', 'lastname': 'Vilches'}
}

'''
/poemas/                /poema/<id>
/calificaciones/        /calificacion/<id>
/usuarios/              /usuario/<id>
'''
class User(Resource):

    def get(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        return user.to_json()

    def delete(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return '', 204

    def put(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(user, key, value)
        db.session.add(user)
        db.session.commit()
        return user.to_json(), 201

class Users(Resource):

    def get(self):
        users = db.session.query(UserModel).all()
        return jsonify([user.to_json() for user in users])

    def post(self):
        user = UserModel.from_json(request.get_json())
        db.session.add(user)
        db.session.commit()
        return user.to_json(), 201