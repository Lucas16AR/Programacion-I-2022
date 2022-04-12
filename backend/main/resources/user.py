from flask_restful import Resource
from flask import request

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
        if int(id) in USERS:
            return USERS[int(id)]
        return '', 404

    def delete(self, id):
        if int(id) in USERS:
            del USERS[int(id)]
            return '', 204
        return '', 404

    def put(self, id):
        if int(id) in USERS:
            User = USERS[int(id)]
            data = request.get_json()
            User.update(data)
            return User, 201
        return '', 404

class Users(Resource):

    def get(self):
        return USERS

    def post(self):
        Users = request.get_json()
        id = int(max(USERS.keys())) + 1
        USERS[id] = Users
        return USERS[id], 201