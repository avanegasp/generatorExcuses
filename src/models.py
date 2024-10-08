from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Excuse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_excuse = db.Column(db.String(200), unique=False, nullable=False)

    def __repr__(self):
        return '<Excuse %r>' % self.user_excuse

    def serialize(self):
        return{
            "id":self.id,
            "excuse": self.user_excuse
        }    