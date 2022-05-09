from .. import db

##################################################################################################################
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    mark = db.relationship('Mark', back_populates = 'user', cascade = "all, delete-orphan")
    poem = db.relationship('Poem', back_populates = 'user', cascade = "all, delete-orphan")

    def __repr__(self):
        # return '<User: %r %r %r %r >' % (self.id, self.firstname, self.password, self.role, self.email)
        return f"""
{self.id}
{self.firstname}
{self.password}
{self.role}
{self.email}
        """

##################################################################################################################

    def to_json(self):
        user_json = {
            'id': self.id,
            'firstname': str(self.firstname),
            'num_poems': len(self.poem),
            'num_marks': len(self.mark),
            'poems': [poem.to_json() for poem in self.poem]
        }
        return user_json
    
    def to_json_short(self):
        user_json = {
            'id': self.id,
            'email': str(self.email)
        }
        return user_json
    
    def to_json_complete(self):
        poem = [poem.to_json() for poem in self.poem]
        mark = [mark.to_json() for mark in self.mark]
        
        user_json = {
            'id': self.id,
            'name': str(self.name),
            'password': str(self.password),
            'role': str(self.rol),
            'email': str(self.email),
            'poem':poem,
            'mark':mark
        }
        return user_json

###########################################################################################

    @staticmethod
    def from_json(user_json):
        id = user_json.get('id')
        firstname = user_json.get('firstname')
        password = user_json.get('password')
        role = user_json.get('role')
        email = user_json.get('email')

        return User(id=id,
                    firstname=firstname,
                    password=password,
                    role=role,
                    email=email
                    )