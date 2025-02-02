from flask import Flask
from flask import request
from flask import jsonify
import json

app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to jacky Web App!'


@app.route('/articles')         # 基本路由
def articles():
    a = dict()
    a["a"] = 123
    a["d"] = dict()
    a["d"]["d1"] = "i am d1"
    a["d"]["d5"] = "i am d5"
    return json.dumps(a)


@app.route('/user/<username>')  # 接收參數
def show_user_profile(username):
    return f'Hi, User: {username}'


@app.route('/login', methods=['GET', 'POST'])   # 處理方法
def login():
    if request.method == 'POST':
        return "login POST"
    elif request.method == 'GET':
        return "login GET"
    else:
        return "login Method unknown"


@app.route('/submit', methods=['GET'])  # 處理Form
def submit_form():
    name = request.form['name']
    email = request.form['email']
    return f"Received: {name}, {email}"


@app.route('/data')                     # json回應
def get_data():
    data = {'name': 'John', 'age': 30}
    return jsonify(data)


@app.route('/upload', methods=['POST'])  # 文件上傳
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        file.save(f"./uploads/{file.filename}")
        return f"File {file.filename} uploaded successfully!"


if __name__ == '__main__':
    app.run(debug=True)
