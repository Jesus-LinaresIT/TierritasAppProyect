from flask import request
from flask_restplus import Namespace, Resource, Api
from ..config import SECRET_KEY
from ..service.user_service import save_new_user, convert_date_time
from ..service.contact_services import save_contacts
from ..model.user import Users
import jwt

api = Namespace('validate', description='user related operations')


@api.route('/')
class ValidateToken(Resource):
    def post(self):
        # valid token
        data = request.get_json()
        data['isActive'] = True

        if 'birthdate' in data:
            data['birthdate'] = convert_date_time(data['birthdate'])

        validate = jwt.decode(data['token'], SECRET_KEY)

        try:
            if validate:
                if data['email'] == validate['email']:
                    if 'isAdmin' in validate:
                        data['isAdmin'] = validate['isAdmin']

                    data_contacts = data['contacts']
                    if data_contacts:
                        del data['contacts']

                    response = save_new_user(data)

                    if not isinstance(response, Users):
                        return response
                      
                    save_contacts(data_contacts, response.id)

                    return {'message': 'En horabuena, te haz registrado exitosamente'}, 200

                else:
                    return {'status': 'Error. El correo ingresado no es valido.'}, 400

        except jwt.InvalidTokenError:
            return {'message': 'Ha ocurrido un error con la aplicación. Contacte con el administrador.'}, 500

