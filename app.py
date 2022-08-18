from main import app
from main.models import db
import sys

if __name__ == '__main__':
    try:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.app = app
        db.init_app(app)
        db.create_all()
        app.debug = True
        app.run()

    except KeyboardInterrupt:
        sys.exit(0)