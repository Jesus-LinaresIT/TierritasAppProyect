from flask import request
from flask_restplus import Resource
from ..util.dto import UserInvite
from ..service.invite_services import generateToken_invite, checkEmail
from ..util.decorators import token_required, admin_token_required

api = UserInvite.api

user_invite = UserInvite.user_invite


@api.route('/')
class userInvite(Resource):

    @api.doc('user invite')
    @api.expect(user_invite, validate=True)
    @admin_token_required
    def post(self):
        # get the post data
        invite = request.get_json()
        if checkEmail(invite['email']):
            print(invite)
            return generateToken_invite(invite)
        else:
            return {'message': 'Verifique que ha escrito correctamente su correo electronico.'}