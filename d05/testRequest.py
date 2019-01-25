from flask import Flask, request
app = Flask(__name__)

@app.route("/request/")
def req():
    print(request)
    print(type(request))
    # 请求方式
    print(request.method)
    print(request.data)
    # Get请求参数 ?后的参数
    print(request.args)
    # Post请求体中的参数
    print(request.form)
    # 上传的文件
    print(request.files)
    # ip
    print(request.remote_addr)
    # 请求者身份
    print(request.user_agent)
    # 请求的url path地址
    print(request.url)

    print(request.args.get("name"))

    return "Test Request!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
