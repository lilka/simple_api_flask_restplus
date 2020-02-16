from flask_restplus import fields
from simple_api.api.restplus import api

user = api.model('User', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a user'),
    'name': fields.String(required=True, description='User name'),
    'surname': fields.String(required=True, description='User surname'),
    'age': fields.Integer,

})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

users = api.model('Users',{
    'users': fields.List(fields.Nested(user))
})


