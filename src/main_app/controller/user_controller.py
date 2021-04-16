from flask import request
from flask_restplus import Resource
from werkzeug.exceptions import BadRequest
from ..util.decorators import token_required, admin_token_required
from ..util.dto import UserDto
from ..model.user import Users
from ..service.contact_services import save_contacts
from ..service.user_service import get_all_users, get_user_by_id, update_user_by_id, delete_user_by_id, save_new_user, \
    convert_date_time

api = UserDto.api

_request = UserDto.request
_response = UserDto.response


@api.route('/')
class UserList(Resource):

    @token_required
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_response, skip_none=True)
    def get(self, **kwargs):
        return get_all_users()

    @token_required
    @api.response(201, 'User succesfully created.')
    @api.doc('create a new user')
    @api.expect(_request, validate=True)
    def post(self):
        # Creates a new User
        data = request.get_json()

        data['isActive'] = True
        data_contacts = data['contacts']
        if data_contacts:
            del data['contacts']

        if 'birthdate' in data:
            data['birthdate'] = convert_date_time(data['birthdate'])

        response = save_new_user(data)
        print(response)
        if isinstance(response, Users):
            return save_contacts(data_contacts, response)


@api.route('/<id>', methods=['DELETE', 'GET', 'PUT'])
@api.param('id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @token_required
    @api.doc('get a user')
    @api.marshal_with(_response)
    def get(self, id):
        return get_user_by_id(id)

    @token_required
    def put(self, id):
        data = request.get_json()
        return update_user_by_id(data, id)

    @admin_token_required
    def delete(self, id):
        return delete_user_by_id(id)
