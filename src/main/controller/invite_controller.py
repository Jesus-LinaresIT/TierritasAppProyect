from flask import request
from flask_restplus import Resource

from ..util.dto import UserInvite
from ..service.invite_services import *
from ..util.decorators import *

api = UserInvite.api

user_invite = UserInvite.user_invite


@api.route('/')
class userInvite(Resource):

    @api.doc('user invite')
    @api.expect(user_invite, validate=True)
 #   @admin_token_required
    def post(self):
        # get the post data
        invite = request.get_json()
        response = generateToken_invite(invite)

        return response