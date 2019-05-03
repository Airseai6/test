#! python3
# -*- coding:utf-8 -*-
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from zlktqa import app
from exts import db

manage = Manager(app)

# use migrate binding app & db
migrate = Migrate(app, db)
# add the command of migrating to manage
manage.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manage.run()
