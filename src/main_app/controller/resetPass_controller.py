from flask import Blueprint, request
from flask_restplus import Namespace, Resource, Api
from ..config import SECRET_KEY
from ..service.user_service import *
from ..service.contact_services import *
from ..model.user import Users
import jwt

api = Namespace('validate', description='user related operations')

@api.route('/')
class ResetPassword(Resource):
    def post(self):
        # valid token
        try:
            data = request.get_json()
            if 'token' in data:
                decodedToken = jwt.decode(data['token'], SECRET_KEY)

                if decodedToken:
                    user = Users.query.filter_by(email=decodedToken['email']).first()

                    if data["new_password"] == data["password_confirm"]:
                        if not checkPassword(data["new_password"]):
                            return {"status": "Verique la seguridad de su contraseña"}

                        user.password = data["new_password"]
                        db.session.commit()

                        return {"status" : "Contraseña cambiada exitosamente"}

                    else:
                        return{"status": "Las contraseñas ingresadas no coinciden o no cumplen los requisitos de seguridad"}

        except jwt.InvalidTokenError:
            return {'status': 'Error',
                    'message': 'Oh, parece que algo anda mal, puedes intentarlo más tarde si lo deseas.'}