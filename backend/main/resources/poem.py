import re
from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import PoemModel, UserModel, UserModel
from datetime import * 
from sqlalchemy import func
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt


####################################################################################

class Poem(Resource):

    @jwt_required()
    def get(self, id):
        poem = db.session.query(PoemModel).get_or_404(int(id))
        return poem.to_json()

    @jwt_required()
    def delete(self, id):
        claims = get_jwt()
        user_id = get_jwt_identity()
        poem = db.session.query(PoemModel).get_or_404()
        if 'role' in claims:
            if claims['role'] == 'admin' or user_id == int(poem.user_id)
            db.session.delete(poem)
            db.session.commit()
            return '', 204
        else:
            return 'Only admin and poets delete poems'

    def put (self, id):
        poem = db.session.query(PoemModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(poem, key, value)
        db.session.add(poem)
        db.session.commit()
        return poem.to_json(), 201 

########################################################################################
class Poems(Resource):

    @jwt_required(optional = True)
    def get(self):
        poems = db.session.query(PoemModel).get_or_404(id)
        page = 1
        per_page = 20
        claims = get_jwt()
        identify_user = get_jwt_identity()
        if identify_user:
            if request.get_json():
                filters = request.get_json().items()
                for key, value in filters:
                    if key == "page":
                        page = int(value)
                    if key == "per_page":
                        per_page = int(value)
            poems = db.session.query(PoemModel).filter(PoemModel.user_id != identify_user)
            poems = poems.outerjoin(PoemModel.marks).group_by(PoemModel.id).order_by(func.count(PoemModel.marks))
        else:
            if request.get_json():
                filters = request.get_json().items()
                if key == "page":
                    page = int(value)
                if key == "per_page":
                    per_page = int(value)
                if key == "title":
                    poems = poems.filter(PoemModel.title.like('%'+value+'%'))
                if key == "user_id":
                    poems = poems.filter(PoemModel.user_id == value)             
                if key == "created[gt]":
                    poems = poems.filter(PoemModel.dateTime >= datetime.strptime(value, '%d-%m-%Y'))
                if key == "created[lt]":
                    poems = poems.filter(PoemModel.dateTime <= datetime.strptime(value, '%d-%m-%Y'))
                if key == "sort_by":
                    if value == "userId":
                        poems = poems.order_by(PoemModel.user)
                    if value == "userID[desc]":
                        poems = poems.order_by(PoemModel.userID.desc())
                    if value == "dateTime":
                        poems == poems.order_by(PoemModel.dateTime)
                    if value == "dateTime[desc]":
                        poems = poems.order_by(PoemModel.dateTime.desc())
                    if value == "marks":
                        poems = poems.outerjoin(PoemModel.marks).group_by(PoemModel.id).order_by(func.avg(PoemModel.score))
                    if value == "marks[desc]":
                        poems = poems.outerjoin(PoemModel.marks).group_by(PoemModel.id).order_by(func.avg(PoemModel.score).desc())
        
        poems = poems.paginate(page, per_page, False, 30)
        
        if "role" in claims:
            if claims["role"] == "admin":
                return jsonify([{
            "poems" : [poem.to_json_short() for poem in poems.items],
            "total" : poems.total,
            "pages" : poems.pages,
            "page" : page
            }])
            else:
                return jsonify({
                "poems":[poem.to_json() for poem in poems.items],
                "total": poems.total, 
                "pages": poems.pages, 
                "page": page
                })

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        poem = PoemModel.from_json(request.get_json())
        user = db.session.query(UserModel).get_or_404(user_id)
        claims = get_jwt()
        if 'role' in claims:
            if claims['role'] == 'poem':
                if len(user.poem) == 0 or len(user.marks) >= 2:
                    db.session.add(poem)
                    db.session.commit()
                    return poem.to_json(), 201
                else:
                    return 'Not enough marks for the user'
            else:
                return 'Only Poets can create poems'