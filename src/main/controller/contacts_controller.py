from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto
from ..service.contact_services import *


api = UserDto.api


@api.route('/<id>', methods = ['DELETE', 'GET', 'PUT'])
@api.param('id', 'The User identifier')
@api.response(404, 'User not found.')
class Contacts(Resource):
    def delete(self, id):
        user = delete_one_contact(id)
        if not user:
            return {'message' : 'Contact not found'}, 404
        else:
            return user

    def put(self, id):
        data = request.get_json()
        return edit_user(data, id)
