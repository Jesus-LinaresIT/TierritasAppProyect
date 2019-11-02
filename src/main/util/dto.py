from flask_restplus import Namespace, fields
import main.util.custom_fields as customfields


class UserDto:
    api = Namespace('user', description='user related operations')
    contacts = api.model('Contact', {
        'id': fields.Integer,
        'name': fields.String(required=True, description='user first_name'),
        'phone': fields.String(required=True, description='user phone')
    })
    response = api.model('User', {
        'id': fields.String,
        'email': fields.String(required=True, description='user email address'),
        'first_name': fields.String(required=True, description='user first_name'),
        'last_name': fields.String(required=True, description='user last_name'),
        'phone': fields.String(required=True, description='user phone'),
        'contacts': fields.List(fields.Nested(contacts))
    })

    request = api.model('User', {
        'email': customfields.Email(required=True, description='user email address'),
        'first_name': fields.String(required=True, description='user first_name'),
        'last_name': fields.String(required=True, description='user last_name'),
        'phone': fields.String(required=True, description='user phone'),
        'password': fields.String(required=True, description='1234'),
        # 'birthday': fields.DateTime(required=True, description='user birthday'),
        'bloodtype': fields.String(required=True, description='user bloodtype'),
        'dui': fields.String(required=True, description='user dui'),
        'health_insurance_type': fields.String(required=True, description='user health_insurance_type'),
        'isActive': fields.Boolean(required=False, description='user isActive'),
        'insurance_company': fields.String(required=True, description='user insurance_company'),
        'insurance_policy': fields.String(required=False, description='user insurance_policy')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': customfields.Email(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class UserInvite:
    api = Namespace('invite', description='authentication related operations')
    user_invite = api.model('user_invite', {
        'email': customfields.Email(required=True, description='The email address'),
        'isAdmin': fields.Boolean(required=False, description='The range user '),
    })
