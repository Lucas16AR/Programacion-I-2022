from xml.etree.ElementTree import Comment
from flask_restful import Resource
from flask import jsonify, request
from .. import db
from main.models import MarkModel

############################################################################################

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

###############################################################################################

class Marks(Resource):

    def get(self):

        marks = db.session.query(MarkModel).all()
        page = 1
        per_page = 20

        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:

                if key == "page":
                    page = int(value)
                if key == "per_page":
                    per_page = int(value)
                if key == "mark":
                    mark = mark.filter(MarkModel.mark == value)
                if key == "comment":
                    comment = comment.filter(MarkModel.comment.like("%" + value + "%"))
                if key == "userID":
                    userID = userID.filter(MarkModel.userID == value)
                if key == "poemID":
                    poemId = poemId.filter(MarkModel.poemID == value)
                
                if key == "sort_by":
                    if value == "mark":
                        mark = mark.order_by(MarkModel.mark)
                    if value == "mark[desc]":
                        mark = mark.order_by(MarkModel.puntaje.desc())
                    if value == "userID":
                        user = user.order_by(MarkModel.userID)
                    if value == "userID[des]":
                        user = user.order_by(MarkModel.userID.desc())
                    if value == "poemID":
                        poem = poem.order_by(MarkModel.poemId)
                    if value == "poemID[des]":
                        poem = poem.order_by(MarkModel.poemId.desc())
        
        marks = marks.paginate(page, per_page, False, 30)
 
        return jsonify([{
                "marks" : [mark.to_json_short() for mark in marks.items],
                "total" : marks.total,
                "pages" : marks.pages,
                "page" : page
                }])

    def post(self):
        mark = MarkModel.from_json(request.get_json())
        db.session.add(mark)
        db.session.commit()
        return mark.to_json(), 201