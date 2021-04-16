from ..config import FRONTEND_URL

def inviteTemplate(invite_token):
     # Create the plain-text and HTML version of your message
    message_text = """\
    {0}/sign-up/{1}"""
    message_html = """\
    <html lang="es">
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1">
    </head>
    
    <body>
    
    <div style=" max-width: 500px; width: 100%; margin: 0 auto; border: 1px solid #ccc; padding: 20px; text-align: center; border-radius: 10px;">
    <img src="{0}/assets/logo.png" alt="">
    <p>Has sido invitado a unirte a <span style="color: #00b0f2;">TIERRITAS MOTO CLUB EL SALVADOR</span>, 
    para poder registrarte con tu correo electrónico ingresa presionando el botón Regístrate a continuación:</p>
    <a style="text-decoration: none; display: inline-block; font: bold 16px1 arial; background: #ff2e34; 
    color: #fff; text-align: center; padding: 15px 20px; margin: 10px 0; cursor: pointer;" href="{0}/sign-up/{1}">REGÍSTRATE</a>
    
    <p>O bien copia y pega el siguiente vínculo en tu navegador:</p>
    <p style="color:#00b0f2;">{0}/sign-up/{1}</p>
    </div>
    
    </body>
    """ 
    return {'text': message_text.format(FRONTEND_URL, invite_token), 'html': message_html.format(FRONTEND_URL, invite_token)}


def ForgotPasswordTemplate(token):
    # Create the plain-text and HTML version of your message
    message_text = """\
    Has solicitado un cambio de contraseña a tu usuario de TIERRITAS MOTO CLUB EL SALVADOR, 
    para poder cambiar tu contraseña copia y pega el siguiente vínculo en tu navegador:
    {0}/reset-password/{1}"""
    
    message_html = """\
    <html lang="es">
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1">
    </head>

    <body>

    <div style=" max-width: 500px; width: 100%; margin: 0 auto; border: 1px solid #ccc; padding: 20px; text-align: center; border-radius: 10px;">
    <img src="{0}/assets/logo.png" alt="">
    <p>Has solicitado un cambio de contraseña a tu usuario de <span style="color: #00b0f2;">TIERRITAS MOTO CLUB EL SALVADOR</span>, 
    para poder cambiar tu contraseña ingresa presionando el botón cambiar contraseña a continuación:</p>
    <a style="text-decoration: none; display: inline-block; font: bold 16px1 arial; background: #ff2e34; 
    color: #fff; text-align: center; padding: 15px 20px; margin: 10px 0; cursor: pointer;" href="{0}/reset-password/{1}">Cambiar contraseña</a>

    <p>O bien copia y pega el siguiente vínculo en tu navegador:</p>
    <p style="color:#00b0f2;">{0}/reset-password/{1}</p>
    </div>

    </body>
    """
    return {'text': message_text.format(FRONTEND_URL, token), 'html': message_html.format(FRONTEND_URL, token)}