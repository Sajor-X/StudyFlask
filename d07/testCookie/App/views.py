from flask import Blueprint, url_for, render_template, request, Response, redirect

blue = Blueprint('first_blue', __name__)

@blue.route('/')
def index():
    return "Hello Flask"

@blue.route('/home/')
def home():
    username = request.cookies.get("user")
    return render_template('home.html', username=username)

@blue.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        username = request.form.get("username")
        resp = Response(response="Login Success: %s" % username)
        resp.set_cookie('user', username)
        return resp
        

@blue.route('/logout/')
def logout():
    resp = redirect(url_for('first_blue.home'))
    resp.delete_cookie('user')
    return resp 
