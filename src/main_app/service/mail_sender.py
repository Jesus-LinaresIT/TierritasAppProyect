from email.mime.text import MIMEText
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from ..config import EMAIL_FROM, EMAIL_PASSWORD

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
    sender_email = EMAIL_FROM
    password = EMAIL_PASSWORD

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
        server.sendmail(sender_email, email_object.email_to, message.as_string()
    )

    return {
        'message': 'Te hemos enviado un correo electónico para cambiar tu contraseña'
    }, 200