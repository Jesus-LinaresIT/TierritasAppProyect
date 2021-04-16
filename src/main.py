#!/usr/bin/env python3
import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from blueprint import bpt
from main_app import create_app, DB as db
from main_app.model import user
from main_app.model import blacklist

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(bpt)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

#@manager.command
def run():
    app.run(host="0.0.0.0", port=8080, ssl_context=('/etc/letsencrypt/live/tierritas.com/fullchain.pem', '/etc/letsencrypt/live/tierritas.com/privkey.pem'))

if __name__ == '__main__':
    # db.create_all()
    run()
