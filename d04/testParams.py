from flask import Flask, url_for
import uuid
app = Flask(__name__)

@app.route("/params/<heh>/", methods=['GET'])
def params(heh):
    print(type(heh))
    print(heh)
    return "Test Params"

@app.route("/getuuid/")
def get_uuid():
    return str(uuid.uuid4())

@app.route("/get/<uuid:name>/")
def get(name):
    print(type(name))
    print(name)
    return "Test UUID"

@app.route("/any/<any(c, d, e):name>/")
def any(name):
    print(type(name))
    print(name)
    return "Test Any"

@app.route("/url/")
def url():
    url = url_for("get_uuid")
    print(url)
    print(type(url))

    anyurl = url_for("any", name="c")
    print(anyurl)

    return "Test UrlFor"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
