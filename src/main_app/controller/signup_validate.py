from flask import Blueprint
from flask_restplus import Namespace, Resource, Api
from ..config import SECRET_KEY
import jwt

api = Namespace('validate', description='user related operations')


@api.route('/<string:token_invite>', methods=['POST', 'GET'])
class ValidateToken(Resource):
    def post(self, token_invite):
        # valid token
        try:
            if token_invite:
                payload = jwt.decode(token_invite, SECRET_KEY)
                if payload:
                    return 'valid'

        except jwt.InvalidTokenError:
            return 'invalid'
