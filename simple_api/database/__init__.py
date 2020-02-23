
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()


def reset_database():
    from simple_api.database.models import User
    db.drop_all()
    db.create_all()
    fill_database()


def fill_database():
    from simple_api.database.models import User
    import json
    from simple_api.api.buisness import create_user

    with open(r"/Users/lilalomnicka/PycharmProjects/spimple_api/simple_api/database/MOCK_DATA.json") as json_file:
        data = json.load(json_file)
        for p in data:
            create_user(p)
