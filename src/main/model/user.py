from .. import db, flask_bcrypt
import datetime as dt
import jwt
#from main.model.blacklist import BlacklistToken
#from ..config import key

class Users(db.Model):
	#User Model for storing user related details
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key = True, autoincrement=True)
	first_name = db.Column(db.String(150))
	last_name = db.Column(db.String(150))
	email = db.Column(db.VARCHAR(200), index = True, unique = True)
	phone = db.Column(db.String(20))
	password_hash = db.Column(db.String(150))
	birthday = db.Column(db.DateTime())
	bloodtype = db.Column(db.VARCHAR(15))
	dui = db.Column(db.VARCHAR(10))
	health_insurance_type = db.Column(db.String(25))
	isAdmin = db.Column(db.Boolean)
	isActive = db.Column(db.Boolean)
	date = db.Column(db.DateTime(timezone=True), default = dt.datetime.utcnow())	
	insurance_company = db.Column(db.VARCHAR(75))
	insurance_policy = db.Column(db.VARCHAR(75))
	image = db.Column(db.VARCHAR(200))

	relationContact = db.relationship('Contact', cascade = 'all,delete', backref = 'users', uselist = False)

	def __init__(self, dictionary):
		for k, v in dictionary.items():

			if hasattr(self, k):			
				setattr(self, k, v)

	def updateProperties(self, dictionary):
		for k, v in dictionary.items():
			if hasattr(self, k):
				setattr(self, k, v)

	@property
	def password(self):
		raise AttributeError('password: write-only field')

	@password.setter
	def password(self, password):
		self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

	def check_password(self, password):
		return flask_bcrypt.check_password_hash(self.password_hash, password)

	def __repr__(self):
		return "<Users '{}'>".format(self.first_name)


class Contact(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	name = db.Column(db.String(150))
	phone = db.Column(db.Integer)

	def __init__(self, dictionary):
	 	for k, v in dictionary.items():
	 		setattr(self, k, v)

	def updatePropertiesC(self, dictionary):
		for k, v in dictionary.items():
			if hasattr(self, k):
				setattr(self, k, v)


"""def encode_auth_token(self):
	print('/////////////////////////////////', self.id)
	try:
		payload = {
			'id': self.id,
			'email': self.email
		}
		return jwt.encode(payload, key, algorithm = 'HS256')

	except Exception as e:
		return e


def decode_auth_token(auth_token):
     
        Decodes the auth token
        :param auth_token:
        :return: integer|string
       
        try:
            payload = jwt.decode(auth_token, key)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'   
"""