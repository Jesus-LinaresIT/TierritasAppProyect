
import os
from datetime import datetime
from ..util.custom_fields import checkEmail, checkPassword
from .. import DB as db
from ..model.user import Users, Contact
from ..service.contact_services import get_contacts, edit_contact
from ..config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS
from flask import send_file
from datetime import date

def convert_date_time(date_time_str):
    return datetime.strptime(date_time_str, '%d-%m-%Y')


def get_all_users():
    try:
        users = Users.query.filter_by(isActive=True).all()

        if not users:
            return 200

        for user in users:
            user.contacts = get_contacts(user.id)

        return users, 200

    except:
        return {'message', 'Ocurrio un error al intentar obtener los usuarios registrados'}, 500


def get_user_by_id(id):
    try:
        user = Users.query.filter_by(id=id).first()

        if not user:
            return 200

        user.contacts = get_contacts(user.id)

        return user, 200

    except:
        return {'message', 'Ocurrio un error al intentar obtener los usuarios registrados'}, 500


def save_new_user(data):
    check_user = Users.query.filter(((Users.dui == data['dui']) | (Users.email == data['email']))).first()

    if check_user:
        return {'message': 'Ya existe un usuario registrado con el dui o correo electrónico introducido'}, 400

    if checkEmail(data['email']):
        if checkPassword(data['password']):
            user = Users(data)
            user.password = data['password']

            try:
                db.session.add(user)
                db.session.commit()

                return user

            except:
                return {'message': 'No se ha podido guardar el usuario ingresado, por favor intente más tarde'}, 500
        else:
            return {'message': 'La contraseña que esta utilizando no es válida'}, 400

    else:        
        return {'message': 'Por favor revise los datos proporcionados y vuelva a intentarlo'}, 400


def update_profile_image(fileName, userId):
    user = Users.query.filter_by(id=userId).first()
    if user:
        data = {'image': fileName}
        print(data)

        try:
            print("SUCCESSSS!!!!!!!!!!!!!")
            user.updateProperties(data)
            db.session.commit()
            return {'message': 'Imagen guardada exitosamente'}, 200
        except:
            return {'message': 'No se pudo guardar la imagen.'}, 400


def update_user_by_id(data, id):
    check_user = Users.query.filter((
            ((Users.dui == data['dui']) | (Users.email == data['email']))
            & (Users.id != id))).first()
    if check_user:
        return {'message': 'Ya existe un usuario registrado con el dui o correo electrónico introducido'}, 400

    user = Users.query.filter_by(id=id).first()

    if user:
        if checkEmail(data['email']):
            try:
                if 'contacts' in data:
                    data_contacts = data['contacts']
                    del data['contacts']

                if 'birthdate' in data:
                    data['birthdate'] = convert_date_time(data['birthdate'])

                user.updateProperties(data)
                db.session.commit()

                if data_contacts:
                    edit_contact(data_contacts, id)

                return {'message': 'Usuario actualizado con éxito'}, 200

            except Exception as e:
                print(e)
                return {'message': 'Ocurrió un error al actualizar los datos, intentelo más tarde'}, 500
        else:
            return {'message': 'El email ingresado no es válido'}, 500

    else:

        return {'message': 'El usuario que esta tratando de editar ya no existe'}, 400


def delete_user_by_id(id):
    user = Users.query.filter_by(id=id).first()
    if user:

        try:
            db.session.delete(user)
            db.session.commit()
            return {'message': 'El usuario ha sido eliminado con éxito'}, 200

        except:
            return {'message': 'Ha ocurrido un error al eliminar el usuario seleccionado'}, 500

    else:
        return {'message': 'El usuario que deseas borrar no existe'}, 404
