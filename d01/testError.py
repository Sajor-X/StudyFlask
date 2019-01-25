from flask import Flask
app = Flask(__name__)
# 创建一个错误函数
@app.route("/testerror/")
def testerror():
    a=5          
    b=0
    c=a/b
                    
app.run(debug=True, host='0.0.0.0', port=5000)
