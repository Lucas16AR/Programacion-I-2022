from email.policy import default
from .. import db
from sqlalchemy.sql import func
from datetime import datetime
import sqlalchemy as sql   
from sqlalchemy import column
import statistics
from statistics import mean

############################################################################################################

class Poem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    body = db.Column(db.String(100), nullable=False)
    dateTime = db.Column(db.DateTime, nullable=False, default=datetime.now())


    user = db.relationship('User', back_populates = "poem", uselist = False, single_parent = True)
    mark = db.relationship('Mark', back_populates = 'poem', cascade = 'all, delete-orphan')

    def __repr__(self):
        return '<Poem: %r %r >' % (self.id, self.title, self.userID, self.body, self.dateTime)

    
    def avg_score(self):
        scoreboard = []
        if len(self.mark) == 0:
            mean = 0
        else:
            for mark in self.mark:
                score = mark.score
                scoreboard.append(score)
            mean = statistics.mean(scoreboard)
        return mean

#######################################################################################################

    def to_json(self):
        poem_json = {
            'id': self.id,
            'title': str(self.title),
            'user': self.user.to_json(),
            'body': str(self.body),
            'dateTime': str(self.dateTime.strftime("%D-%M-%Y")),
            'mark': [mark.to_json() for mark in self.mark],
            'avg_score': self.avg_score()
        }
        return poem_json


    def to_json_short(self):
        poem_json = {
            'id': self.id,
            'title': str(self.title),
            'body': str(self.body)
        }
        return poem_json

#######################################################################################################

    @staticmethod
    def from_json(poem_json):
        id = poem_json.get('id')
        title = poem_json.get('title')
        userID = poem_json.get('userID')
        body = poem_json.get('body')
        dateTime = poem_json.get('dateTime')

        return Poem(id=id,
                    title=title,
                    userID=userID,
                    body=body,
                    dateTime=dateTime
                    )