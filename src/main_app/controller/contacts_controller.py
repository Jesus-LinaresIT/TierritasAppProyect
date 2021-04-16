from flask import request
from flask_restplus import Resource
from ..util.dto import UserDto
from ..service.contact_services import delete_one_contact


api = UserDto.api


@api.route('/<id>', methods=['DELETE', 'PUT'])
@api.param('id', 'The User identifier')
@api.response(404, 'User not found.')
class Contacts(Resource):
    def delete(self, id):
        return delete_one_contact(id)

