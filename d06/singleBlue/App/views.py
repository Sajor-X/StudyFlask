from flask import Blueprint

blue = Blueprint('first_blue', __name__)

@blue.route('/')
def single_flask():
    return "Hello Blueprint"
