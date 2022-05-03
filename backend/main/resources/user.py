from flask_restful import Resource
from flask import jsonify, request
from .. import db
from main.models import UserModel
from sqlalchemy import func

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
        
        page = 1
        per_page = 20
        users = db.session.query(UserModel).all()
        
        if request.get_json():
            filters = request.get_json().items()
            
            for key, value in filters:
                
                if key =="page":
                    page = int(value)
                if key == "per_page":
                    per_page = int(value)
                if key == "name":
                    users=users.filter(UserModel.name.like("%"+value+"%"))
                
                if key == "sort_by":
                
                    if key == "name":
                        users=users.filter(UserModel.name.like("%"+value+"%"))
                    if value == "id_poems[desc]":
                        users=users.outerjoin(UserModel.projects).group_by(UserModel.id).order_by(func.count(UserModel.id).desc())
                    if value == "num_poems":
                        users=users.outerjoin(UserModel.projects).group_by(UserModel.id).order_by(func.count(UserModel.id))
                    if value == "num_marks":
                        users=users.outerjoin(UserModel.firstname)
        
        users = users.paginate(page, per_page, False, 30)
                
        return jsonify({
                'users': [professor.to_json() for professor in users.items],
                'total': users.total,
                'pages': users.pages,
                'page': page
                })




    def post(self):
        user = UserModel.from_json(request.get_json())
        db.session.add(user)
        db.session.commit()
        return user.to_json(), 201