from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    contacts = api.model('Contact', {
        'id': fields.Integer,
        'name': fields.String(required=False, description='user first_name'),
        'phone': fields.String(required=False, description='user phone')
    })

    response = api.model('User', {
        'id': fields.Integer,
        'email': fields.String(description='user email address'),
        'first_name': fields.String(description='user first_name'),
        'last_name': fields.String(description='user last_name'),
        'phone': fields.String( description='user phone'),
        'birthdate': fields.DateTime(description='user birthdate'),
        'bloodtype': fields.String( description='user bloodtype'),
        'dui': fields.String( description='user dui'),
        'health_insurance_type': fields.String( description='user health_insurance_type'),
        'insurance_company': fields.String(description='user insurance_company'),
        'insurance_policy': fields.String(description='user insurance_policy'),
        'image':  fields.String(description='user image'),
        'contacts': fields.List(fields.Nested(contacts, skip_none= True))
    })

    request = api.model('User', {
        'email': fields.String(required=True, description='user email address'),
        'first_name': fields.String(required=True, description='user first_name'),
        'last_name': fields.String(required=True, description='user last_name'),
        'phone': fields.String(required=True, description='user phone'),
        'password': fields.String(required=True, description='1234'),
        'birthdate': fields.DateTime(required=True, description='user birthdate'),
        'bloodtype': fields.String(required=True, description='user bloodtype'),
        'dui': fields.String(required=True, description='user dui'),
        'health_insurance_type': fields.String(required=True, description='user health_insurance_type'),
        'isActive': fields.Boolean(required=False, description='user isActive'),
        'insurance_company': fields.String(required=False, description='user insurance_company'),
        'insurance_policy': fields.String(required=False, description='user insurance_policy'),
        'contacts': fields.List(fields.Nested(contacts, skip_none= True)),
        'image':  fields.String(required=False, description='user image')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class UserInvite:
    api = Namespace('invite', description='authentication related operations')
    user_invite = api.model('user_invite', {
        'email': fields.String(required=True, description='The email address'),
        'isAdmin': fields.Boolean(required=False, description='The range user '),
    })

class UserForgot:
    api = Namespace('forgot', description='authentication related operations')
    forgot_pass = api.model('forgot_pass', {
        'password': fields.String(required=True, description='The user password '),
        'password confirm': fields.String(required=True, description='The user password ')
    })
