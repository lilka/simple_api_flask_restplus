
from simple_api.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    surname = db.Column(db.String(80))
    age = db.Column(db.Integer)



    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


    def __repr__(self):
        return '<User %r>' % self.surname
