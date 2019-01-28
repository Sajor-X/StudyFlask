from flask import Flask
from flask_script import Manager

from App.models import init_db
from App.views import blue

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zzx@localhost:3306/FlaskModel'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(blueprint=blue)

# db = SQLAlchemy(app=app)

init_db(app)

manager = Manager(app=app)


if __name__ == '__main__':
    manager.run()
