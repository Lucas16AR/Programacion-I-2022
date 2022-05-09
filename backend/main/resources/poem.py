from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import PoemModel, UserModel, UserModel
from datetime import * 
from sqlalchemy import func

####################################################################################

class Poem(Resource):

    def get(self, id):
        poem = db.session.query(PoemModel).get_or_404(int(id))
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

########################################################################################
class Poems(Resource):

    def get(self):

        poems = db.session.query(PoemModel).get_or_404(id)
        page = 1
        per_page = 20

        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
        
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
        
        return jsonify([{
            "poems" : [poem.to_json_short() for poem in poems.items],
            "total" : poems.total,
            "pages" : poems.pages,
            "page" : page
            }])


    def post(self):
        poem = PoemModel.from_json(request.get_json())
        db.session.add(poem)
        db.session.commit()
        return poem.to_json(), 201
        return 201 