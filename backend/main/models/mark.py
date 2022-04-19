from .. import db


class Mark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(100), nullable=False)
    userID = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    poemaID = db.Column(db.Integer, db.ForeignKey("poema.id"), nullable=False)
    
    user = db.relationship('User', back_populates ="marks", uselist= False, single_parent = True)
    poem = db.relationship('Poem', back_populates = 'marks', uselist = False, single_parent = True)

    def __repr__(self):
        return '<Mark: %r %r %r %r >' % (self.id, self.score, self.comment, self.userID, self.poemaID)

    def to_json(self):
        mark_json = {
            'id': self.id,
            'score': str(self.score),
            'comment': str(self.comment),
            'userID': str(self.userID),
            'poemaID': str(self.poemaID)
        }
        return mark_json
    
    def to_json_complete(self):
        poem = [poem.to_json() for poem in self.poem]
        user = [user.to_json() for user in self.user]
        mark_json = {
            'id': self.id,
            'name': str(self.name),
            'password': str(self.password),
            'role': str(self.rol),
            'email': str(self.email),
            'poem':poem,
            'user':user
        }
        return mark_json


    @staticmethod

    def from_json(mark_json):
        id = mark_json.get('id')
        score = mark_json.get('score')
        comment = mark_json.get('comment')
        userID = mark_json.get('userID')
        poemaID = mark_json.get('poemaID')

        return Mark(id=id,
                    score=score,
                    comment=comment,
                    userID=userID,
                    poemaID=poemaID
                    )