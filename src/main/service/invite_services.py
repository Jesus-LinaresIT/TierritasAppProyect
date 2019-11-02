from ..config import SECRET_KEY
from ..util.decorators import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from main.model.blacklist import BlacklistToken
from ..util.emails import *
import datetime as dt
import smtplib, ssl
import jwt


def generateToken_invite(invite):
    try:
        # generate the auth token
        invite_token = encode_invite_token(invite)

        response_object = {
            'status': 'success',
            'message': 'Invitacion Enviada.',
            'Authorization': invite_token.decode()
        }
        email_template = inviteTemplate(invite_token.decode())
        email_object = EmailObject({
            'email_to': invite['email'],
            'subject': 'Invitacion',
            'message_text': email_template['text'],
            'message_html': email_template['html']
        })
        return send_email(email_object)


    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'There is an error generating token, please verify'
        }

        return response_object, 401


def encode_invite_token(invite):
    try:
        payload = {
            'exp': dt.datetime.utcnow() + dt.timedelta(weeks=1),
            'iat': dt.datetime.now().timestamp(),
            'email': invite['email'],
            'isAdmin': invite['isAdmin']
        }

        return jwt.encode(
            payload,
            SECRET_KEY,
            algorithm='HS256'
        )

    except Exception as e:
        return e


def decode_invite_token(invite_token):
    try:
        payload = jwt.decode(invite_token, SECRET_KEY)
        is_blacklisted_token = BlacklistToken.check_blacklist(invite_token)

        if is_blacklisted_token:
            return 'El usuario con email %s no tiene una sesión activa' % (payload['email'])
        else:
            return is_blacklisted_token
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'

    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'


class EmailObject():
    email_to = ''
    subject = ''
    message_text = ''
    message_html = ''

    def __init__(self, dictionary):
        for k, v in dictionary.items():
            if hasattr(self, k):
                setattr(self, k, v)


def send_email(email_object: EmailObject):
    sender_email = "albertolinares001@gmail.com"
    password = ('hola.alberto126')

    message = MIMEMultipart("alternative")
    message["Subject"] = email_object.subject
    message["From"] = sender_email
    message["To"] = email_object.email_to

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(email_object.message_text, "plain")
    part2 = MIMEText(email_object.message_html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, email_object.email_to, message.as_string()
        )
