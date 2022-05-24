from xml.etree.ElementTree import Comment
from flask_restful import Resource
from flask import jsonify, request
from .. import db
from main.models import MarkModel
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

############################################################################################

class Mark(Resource):

    @jwt_required()
    def get(self, id):
        mark = db.session.query(MarkModel).get_or_404(id)
        return mark.to_json()

    @jwt_required()
    def delete(self, id):
        claims = get_jwt()
        user_id = get_jwt_identity
        mark = db.session.query(MarkModel).get_or_404(id)
        if 'role' in claims:
            if claims['role'] == 'admin' or user_id == mark.user_id:
                db.session.delete(mark)
                db.session.commit()
                return '', 204
            else:
                return 'Only admin and poets are allowed to delete marks'
        
    @jwt_required()
    def put(self, id):
        user_id = get_jwt_identity()
        mark = db.session.query(MarkModel).get_or_404(id)
        if user_id == mark.user_id:
            data = request.get_json().items()
            for key, value in data:
                setattr(mark, key, value)
            db.session.add(mark)
            db.session.commit()
            return mark.to_json(), 201
        else:
            return 'Only admin and poets are allowed to update marks'

###############################################################################################

class Marks(Resource):

    @jwt_required()
    def get(self):
        marks = db.session.query(MarkModel).all()
        return jsonify({[mark.to_json() for mark in marks]})


    @jwt_required()
    def post(self):
        mark = MarkModel.from_json(request.get_json())
        db.session.add(mark)
        db.session.commit()
        return mark.to_json(), 201