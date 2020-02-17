import logging

from flask import request
from flask_restplus import Resource

from simple_api.api.buisness import create_user, delete_user, update_user
from simple_api.api.restplus import api
from simple_api.database.models import User

from simple_api.serializers import user

log = logging.getLogger(__name__)

ns = api.namespace('user', description='Operations related to user')


@ns.route('/')
class UsersCollection(Resource):

    @api.marshal_with(user)
    def get(self):
        """
        Returns list of users.
        # """

        return User.query.all()

    @api.expect(user)
    def post(self):
        """
        Creates new user.
        """
        create_user(request.json)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'User not found.')
class UserItem(Resource):

    @api.marshal_with(user)
    def get(self, id):
        """
        Returns the user.
        """
        return User.query.filter(User.id == id).one()

    @api.expect(user)
    @api.response(204, 'User successfully updated.')
    def put(self, id):
        """
        Updates the user.
        """
        data = request.json
        update_user(id, data)
        return None, 204

    @api.response(204, 'User successfully deleted.')
    def delete(self, id):
        """
        Deletes the user.
        """
        delete_user(id)
        return None, 204
