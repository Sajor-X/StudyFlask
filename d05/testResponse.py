from flask import Flask, request, make_response, Response, url_for, redirect, abort, json
app = Flask(__name__)

@app.route("/response1/")
def resp1():
    html = "<h1>Test Request!</h1>"
    response = make_response(html, 404)
    print(response)
    print(type(response))
    return response

@app.route("/response2/")
def resp2():
    html = "<h1>Test Request!</h1>"
    response = Response(html, 404)
    print(response)
    print(type(response))
    return response

@app.route("/redirect/")
def redir():
    response = redirect(url_for('resp1'))
    print(response)
    print(type(response))
    return response

@app.route("/abort/")
def ab():
    abort(403)

@app.route("/json/")
def json_test():
    json_data = {"name": "123"} 
    return json.jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
