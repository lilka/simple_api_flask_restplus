from simple_api.database import reset_database
from simple_api.app import  app, initialize_app
initialize_app(app)
with app.app_context():
    reset_database()