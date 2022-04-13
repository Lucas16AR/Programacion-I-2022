from email.policy import default
from .. import db
from sqlalchemy.sql import func

class Poem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    userID = db.Column(db.Integer, nullable=False)
    body = db.Column(db.String(100), nullable=False)
    dateTime = db.Column(db.DateTime(timezone=True), default=func.now())

    def __repr__(self):
        return '<Poem: %r %r >' % (self.id, self.title, self.userID, self.body, self.dateTime)

    def to_json(self):
        poem_json = {
            'id': self.id,
            'title': str(self.title),
            'userID': str(self.userID),
            'body': str(self.body),
            'dateTime': str(self.dateTime),

        }
        return poem_json

    def to_json_short(self):
        poem_json = {
            'id': self.id,
            'title': str(self.title),
            'userID': str(self.userID),
            'body': str(self.body),
            'dateTime': str(self.dateTime),
        }
        return poem_json
    
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