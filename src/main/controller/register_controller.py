from flask import Blueprint, request
from flask_restplus import Namespace, Resource, Api
from main.config import SECRET_KEY
import jwt

api = Namespace('validate', description='user related operations')


@api.route('/validate/<string:token_invite>', methods=['POST', 'GET'])
class Register(Resource):
    def post(self, token_invite):
        # valid token
        try:
            if token_invite:
                payload = jwt.decode(token_invite, SECRET_KEY)
                if payload:
                    return{'email': payload['email'], 'token_invite' : token_invite }

        except jwt.InvalidTokenError:
            return {'status': 'fail',
                    'message': 'Token ingresado no valido o ha espirado.'}

