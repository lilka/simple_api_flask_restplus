
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()


def reset_database():
    from simple_api.database.models import User
    db.drop_all()
    db.create_all()
