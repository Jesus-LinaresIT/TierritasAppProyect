from .. import DB as db, flask_bcrypt
import datetime as dt
import jwt
from ..model.blacklist import BlacklistToken
from ..config import SECRET_KEY


class Users(db.Model):
	# User Model for storing user related details
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key = True, autoincrement=True)
	first_name = db.Column(db.String(150))
	last_name = db.Column(db.String(150))
	email = db.Column(db.VARCHAR(200), index=True, unique=True)
	phone = db.Column(db.String(20))
	password_hash = db.Column(db.String(150))
	birthdate = db.Column(db.DateTime())
	bloodtype = db.Column(db.VARCHAR(15))
	dui = db.Column(db.VARCHAR(10), unique = True)
	health_insurance_type = db.Column(db.String(30))
	isAdmin = db.Column(db.Boolean)
	isActive = db.Column(db.Boolean)
	date = db.Column(db.DateTime(timezone=True), default = dt.datetime.utcnow())	
	insurance_company = db.Column(db.VARCHAR(75))
	insurance_policy = db.Column(db.VARCHAR(75))
	image = db.Column(db.String(25))

	relationContact = db.relationship('Contact', cascade = 'all,delete', backref = 'users', uselist = True)

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


	def encode_auth_token(self, user):
		try:
			payload = {
				'exp': dt.datetime.utcnow() + dt.timedelta(hours=2),
				'iat': dt.datetime.now().timestamp(),
				'user_id': user.id, 
				'email' : user.email,
				'isAdmin' : user.isAdmin
			}

			return jwt.encode(
					payload,
					SECRET_KEY,
					algorithm='HS256'
			)

		except Exception as e:
			return e

	@staticmethod
	def decode_auth_token(auth_token):		
		try:
			payload = jwt.decode(auth_token, SECRET_KEY)
			
			is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)

			if is_blacklisted_token:
				return 'El usuario con email %s no tiene una sesión activa'% (payload['email'])
			else:
				return payload

		except jwt.ExpiredSignatureError:
			return 'Signature expired. Please log in again.'

		except jwt.InvalidTokenError:
			return 'Invalid token. Please log in again.'


class Contact(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	name = db.Column(db.String(150))
	phone = db.Column(db.Integer)

	def __init__(self, dictionary):
		for k, v in dictionary.items():
			setattr(self, k, v)

	def updateProperties(self, dictionary):
		for k, v in dictionary.items():
			if hasattr(self, k):
				setattr(self, k, v)
