# coding:utf-8
import os, io
import PIL
from PIL import Image
from flask_restplus import Resource, Namespace, Api
from ..util.decorators import *
from ..service.auth_helper import Auth
from ..service.user_service import update_profile_image
from flask import Flask, request, redirect, url_for, Response, render_template, \
    send_file, make_response, jsonify, send_from_directory
from werkzeug import secure_filename
from ..config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS

api = Namespace('upload', description='user related operations')
app = Flask(__name__)


@api.route('/', methods=['POST'])
@api.route('/<name>', methods=['GET'])
class Images(Resource):
    @staticmethod
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

    @staticmethod
    def create_thumbnail(image):
        try:
            base_width = 250
            path = "".join([UPLOAD_FOLDER, image])
            img = Image.open(path)
            w_percent = (base_width / float(img.size[0]))
            h_size = int((float(img.size[1]) * float(w_percent)))
            img = img.resize((base_width, h_size), PIL.Image.AFFINE)
            img.save(path)
            return send_file(path)
        except Exception as e:
            print(e)
            return {'message': 'Error al guardar el thumbnail'}, 500

    @token_required
    def post(self):
        if request.method == 'POST':
            
            authToken = Auth.get_logged_in_user(request)
            file = request.files['image']
            if file and self.allowed_file(file.filename):
                try:
                    if not os.path.isdir(UPLOAD_FOLDER):
                        os.mkdir(UPLOAD_FOLDER)
                        
                    name = file.filename.split('.')
                    userId = authToken[0]['data']['user_id']
                    fileName = 'profile_%s.%s' % (userId, name[len(name) - 1])
                       
                    destination = "".join([UPLOAD_FOLDER, fileName])
                    file.save(destination)
                    
                    update_profile_image(fileName, userId)
                               
                    return self.create_thumbnail(fileName)

                except Exception as e:
                    print(e)
                    return ""

    def get(self, name):       
        if name == 'null':
            return send_file(os.path.join(UPLOAD_FOLDER, 'avatar.png'))

        return send_file("".join([UPLOAD_FOLDER, name]))
