from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app=app)

@app.route('/')
def index():
    return "Hello Flask"

manager.run()
