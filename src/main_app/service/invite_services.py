from .mail_sender import send_email, EmailObject
from ..util.emails import inviteTemplate
from ..model.user import Users
from ..util.custom_fields import checkEmail
from .auth_helper import Auth

def generateToken_invite(invite):
    
    if 'email' not in  invite: 
        return {'message': 'Parece que no tienes una invitación valida para el link utilizado'}, 400
    
    emailExist = Users.query.filter_by(email=invite['email']).first()

    if emailExist:
        return {'message': 'Ya existe un usuario registrado con este correo electrónico introducido'}, 400
    
    try:

        # generate the auth token
        exp = 24 * 7
        invite_token = Auth.encode_token(invite, exp, True)

        email_template = inviteTemplate(invite_token.decode())

        send_email(
            EmailObject({
            'email_to': invite['email'],
            'subject': 'Haz sido invitado a unirte a Tierritas Moto Club',
            'message_text': email_template['text'],
            'message_html': email_template['html']
            })
        )

        return {'message': 'Invitacion Enviada.',  'Authorization': invite_token.decode()}, 200

    except:
        return { 'message': 'Ha ocurrido un error inesperado por favor intetelo mas tarde.'}, 500

