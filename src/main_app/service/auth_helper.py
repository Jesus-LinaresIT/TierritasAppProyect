import jwt
import datetime as dt
from ..model.user import Users
from ..service.blacklist_service import save_token
from ..config import SECRET_KEY

class Auth:

    @staticmethod
    def login_user(data):
        try:
            # fetch the user data
            user = Users.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
                auth_token = user.encode_auth_token(user)
                if auth_token:
                    return {
                        'Authorization': auth_token.decode()
                    }, 200
            else:                
                return {
                    'message': 'El correo electrónico y/o contraseña no coinciden con nuestros registros'
                }, 401

        except Exception as e:
            print(e)
            return {
                'message': 'Ha ocurrido un error inesperado, intentalo nuevamente más tarde'
            }, 500


    @staticmethod
    def logout_user(data):
        if data:
            auth_token = data.split(" ")[0]
        else:
            auth_token = ''

        if auth_token:
            resp = Users.decode_auth_token(auth_token)

            if resp:
                return {
                    'message': resp
                }, 401
            else:
                return save_token(token=auth_token)

        else:
            return {
                'message': 'No se ha encontrado un token válido'
            }, 403

    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')

        if auth_token:
            resp = Users.decode_auth_token(auth_token)

            if isinstance(resp, str):
                return {
                    'message': resp
                }, 401
            
            user = Users.query.filter_by(id=resp['user_id']).first()
            
            return {
                'data': {
                    'user_id': user.id,
                    'email': user.email,
                    'isAdmin': user.isAdmin
                }
            }, 200

            
        else:
            return {
                'message': 'No se ha encontrado un token válido'
            }, 401

    
    @staticmethod
    def encode_token(invite, exp = 2, checkAdmin = False):
        try:
            payload = {
                'exp': dt.datetime.utcnow() + dt.timedelta(weeks=exp),
                'iat': dt.datetime.now().timestamp(),
                'email': invite['email']
            }
            
            if checkAdmin: 
                if 'isAdmin' in invite:
                    payload['isAdmin'] = invite['isAdmin']

            return jwt.encode(
                payload,
                SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e

