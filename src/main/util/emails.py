

def inviteTemplate(invite_token):
     # Create the plain-text and HTML version of your message
    message_text = """\
    http://www.tierritas.com/register/{0}"""
    message_html = """\
    <html lang="es">
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1">
    </head>
    
    <body>
    
    <div style=" max-width: 500px; width: 100%; margin: 0 auto; border: 1px solid #ccc; padding: 20px; text-align: center; border-radius: 10px;">
    <img src="http://asesoriait.com/img/logo.png" alt="">
    <p>Has sido invitado a unirte a <span style="color: #00b0f2;">TIERRITAS MOTO CLUB EL SALVADOR</span>, 
    para poder registrarte con tu correo electrónico ingresa presionando el botón Regístrate a continuación:</p>
    <a style="text-decoration: none; display: inline-block; font: bold 16px1 arial; background: #ff2e34; 
    color: #fff; text-align: center; padding: 15px 20px; margin: 10px 0; cursor: pointer;" href="http://www.tierritas.com.sv/register/{0}">REGÍSTRATE</a>
    
    <p>O bien copia y pega el siguiente vínculo en tu navegador:</p>
    <p style="color:#00b0f2;">http://www.tierritas.com.sv/register/{0}</p>
    </div>
    
    </body>
    """ 
    return {'text': message_text.format(invite_token), 'html': message_html.format(invite_token)}

