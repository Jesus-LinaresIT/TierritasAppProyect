from ..util.emails import ForgotPasswordTemplate
from .mail_sender import send_email, EmailObject
from ..model.user import Users
from ..service.auth_helper import Auth
from ..util.custom_fields import checkEmail

def send_forgot_email(payload):

    if not checkEmail(payload['email']):
        return {"messages": "Debes especificar un correo electrónico en formato válido"}, 400
    
    profile_user = Users.query.filter((Users.email == payload['email'])).first()
    print(profile_user)
    if not profile_user:
        return {"message": "El usuario que haz ingresado no existe en nuestros registros"}, 400
            

    try:
        # generate the auth token
        token = Auth.encode_token(payload, 2, False)
        email_template = ForgotPasswordTemplate(token.decode())
        email_object = EmailObject({
            'email_to': payload['email'],
            'subject': '[Tierritas Moto Club] Cambio de contraseña',
            'message_text': email_template['text'],
            'message_html': email_template['html']
        })

        return send_email(email_object)

    except Exception as e:
        print(e)
        return {
            'message': 'Hubo un error al enviar el correo, favor intentarlo más tarde.' 
        }, 400

    