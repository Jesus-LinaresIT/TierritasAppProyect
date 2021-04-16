from flask import Blueprint
from flask_restplus import Api
from flask_cors import CORS

from main_app.controller.user_controller import api as user_ns
from main_app.controller.auth_controller import api as user_auth
from main_app.controller.contacts_controller import api as contact_ns
from main_app.controller.invite_controller import api as user_invite
from main_app.controller.signup_validate import api as signup_validate
from main_app.controller.registry_controller import api as user_registry
from main_app.controller.forgot_controller import api as forgot_pass
from main_app.controller.resetPass_controller import api as reset_password
from main_app.controller.image_controller import api as image_ns

bpt = Blueprint('api', __name__)
CORS(bpt, resource=r'/*')

authorizations = {
    'apiKey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(bpt,
          title = 'Tierritas Api RestFul',
          version = '1.0',
          description= '',
          authorizations= authorizations
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(contact_ns, path='/contact')
api.add_namespace(user_auth, path='/auth')
api.add_namespace(user_invite, path='/invite')
api.add_namespace(signup_validate, path='/validate')
api.add_namespace(user_registry, path='/signup')
api.add_namespace(forgot_pass, path='/forgot-password')
api.add_namespace(reset_password, path='/reset-password')
api.add_namespace(image_ns, path='/images')
