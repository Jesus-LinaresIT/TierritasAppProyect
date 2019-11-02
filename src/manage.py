import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from blueprint import bpt
from main import create_app, db
from main.model import user
from main.model import blacklist

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(bpt)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(host='0.0.0.0', port=9000)


if __name__ == '__main__':
    manager.run()
