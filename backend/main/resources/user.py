from flask_restful import Resource
from flask import jsonify, request
from .. import db
from main.models import UserModel 
from sqlalchemy import func
from datetime import *
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.decorator import admin_required

############################################################################################

class User(Resource):

    @jwt_required
    def get(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        return user.to_json()

    @admin_required
    def delete(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return '', 204

    @jwt_required
    def put(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(user, key, value)
        db.session.add(user)
        db.session.commit()
        return user.to_json(), 201

##############################################################################################

class Users(Resource):

    @admin_required
    def get(self):
        
        page = 1
        per_page = 20
        users = db.session.query(UserModel).all()
        
        if request.get_json():
            filters = request.get_json().items()
            
            for key, value in filters:
                
                if key == "name":
                    users = users.filters(UserModel.name.like('%'+value+'%'))
                if key == "email":
                    email = email.filters(UserModel.email.like('%'+value+'%'))
                if key == "sort_by":
                    if key == "name":
                        users = users.order_by(UserModel.name)              
                    if value == "name[desc]":
                        name = name.order_by(UserModel.name.desc())
                    if key == "email":
                        email = email.order_by(UserModel.name)              
                    if value == "email[desc]":
                        email = email.order_by(UserModel.email.desc())


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