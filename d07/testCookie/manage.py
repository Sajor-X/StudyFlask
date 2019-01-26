from flask import Flask
from flask_script import Manager
from flask_session import Session
from App.views import blue

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Study Flask'
app.config['SESSION_TYPE'] = 'redis'
Session(app)

app.register_blueprint(blueprint=blue)
manager = Manager(app=app)

if __name__ == "__main__":
    manager.run()
