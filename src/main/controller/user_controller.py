from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto
from ..service.user_service import *
from ..service.contact_services import *  

api = UserDto.api
_request = UserDto.request
_response = UserDto.response


@api.route('/')
class UserList(Resource):
	@api.doc('list_of_registered_users')
	@api.marshal_list_with(_response, envelope = 'data')
	def get(self, **kwargs):
		#List all registered users
		users = get_all_users()
		if not users:
			api.abort(404)
		else:
			for user in users:
				user.contacts = get_contacts(user.id)
			return users


	@api.response(201, 'User succesfully created.')
	@api.doc('create a new user')
	@api.expect(_request, validate = True)
	def post(self):
	#Creates a new User
		data = request.get_json()
		data_contacts = data['contacts']
		if data_contacts:
			del data['contacts']

		user = save_new_user(data)

		return save_contacts(data_contacts, user)



@api.route('/<id>', methods = ['DELETE', 'GET', 'PUT'])
@api.param('id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_response)
    def get(self, id):
        #get a user given its identifier
        user = get_a_user(id)
        if not user:
            api.abort(404)
        else:
        		user.contacts = get_contacts(id)
        		return user

    def put(self, id):
        data = request.get_json()
        return edit_user(data, id)
        
    def delete(self, id):
    	user = delete_one_user(id)
    	if not user:       
    		api.abort(404)
    	else:
    		return user