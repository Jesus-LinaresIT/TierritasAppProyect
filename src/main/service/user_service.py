import re
import datetime as dt

from main import db
from main.model.user import Users, Contact

def save_new_user(data, token_invite):
    check_user = Users.query.filter_by(dui = data['dui']).first() or Users.query.filter_by(email = data['email']).first()

    if not check_user:
        user = Users(data)
        user.password = data['password']

        try:
            db.session.add(user)
            db.session.commit()
            return user

        except Exception as e:
            return {'message' : str(e)}
    
    return {'message' : 'Ya existe un usuario registrado con el dui o correo electrónico introducido'}


def delete_one_user(id):
    user = Users.query.filter_by(id = id).first()
    if user:
        db.session.delete(user)
        db.session.commit()

        response_object = {
            'status': 'success',
            'message': 'Successfully eliminated.'
        }
        return response_object, 201


def edit_user(data, id):
    user = Users.query.filter_by(id = id).first()
    if user:
        user.updateProperties(data)

        try:
            db.session.commit()
            response_object = {
                'status': 'Success',
                'message': 'User updated successfully.'
            }
            return response_object, 201
        except:
            response_object = {
                'status': 'Fail',
                'message': 'The user does not exist'
            }
            return response_object, 400
            


def get_all_users():
    return Users.query.filter_by(isActive = True).all()


def get_a_user(id):
    return Users.query.filter_by(id=id).first()



def generate_token(user):
    try:
    # generate the auth token
        auth_token = user.encode_auth_token(user)

        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }

        return response_object, 201

    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'There is an error generating token, please verify'
        }

        return response_object, 401
