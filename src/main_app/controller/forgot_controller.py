from flask import request
from flask_restplus import Namespace, Resource, Api
from ..service.forgot_service import send_forgot_email


api = Namespace('forgot', description='user related operations')


@api.route('/')
class ForgotPassword(Resource):
    def post(self):
        # get the post data
        payload = request.get_json()
        
        return send_forgot_email(payload)