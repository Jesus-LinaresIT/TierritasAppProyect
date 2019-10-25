from flask import request
from flask_restplus import Resource

from ..util.dto import ContactDto
from ..service.contact_services import *


api = ContactDto.api
_request = ContactDto.request
_response = ContactDto.response


@api.route('/<id>', methods = ['DELETE', 'GET', 'PUT'])
@api.param('id', 'The User identifier')
@api.response(404, 'User not found.')
class Contacts(Resource):
     
    def delete(self, user_id):
    	user = delete_one_contact(user_id)
    	if not user:       
    		api.abort(404)
    	else:
    		return user

    def put(self, id):
        data = request.get_json()
        return edit_user(data, id)
