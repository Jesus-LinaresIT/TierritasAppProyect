from flask import Blueprint
from flask_restplus import Api

from main.controller.auth_controller import api as user_auth
from main.controller.contacts_controller import api as contact_ns
from main.controller.invite_controller import api as user_invite
from main.controller.user_controller import api as user_ns
from main.controller.register_controller import api as user_register

bpt = Blueprint('api', __name__)

api = Api(bpt,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(contact_ns, path='/contact')
api.add_namespace(user_auth, path='/auth')
api.add_namespace(user_invite, path='/invite')
api.add_namespace(user_register, path='/register')
