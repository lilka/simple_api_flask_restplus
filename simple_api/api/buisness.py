from simple_api.database import db
from simple_api.database.models import User


def create_user(data):
    name = data.get('name')
    surname = data.get('surname')
    age = data.get('age')
    user = User(name, surname, age)
    db.session.add(user)
    db.session.commit()


def update_user(user_id, data):
    user = User.query.filter(User.id == user_id).one()
    user.name = data.get('name')
    user.surname = data.get('surname')
    user.age = data.get('age')
    db.session.add(user)
    db.session.commit()


def delete_user(user_id):
    user = User.query.filter(User.id == user_id).one()
    db.session.delete(user)
    db.session.commit()
