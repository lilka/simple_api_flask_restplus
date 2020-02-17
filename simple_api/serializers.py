from flask_restplus import fields
from simple_api.api.restplus import api

user = api.model('User', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a user'),
    'name': fields.String(required=True, description='User name'),
    'surname': fields.String(required=True, description='User surname'),
    'age': fields.Integer,

})


