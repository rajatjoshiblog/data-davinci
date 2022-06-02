from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/findsquare/<int:getnum>')
def squarefunc(getnum):
    return f'Square is {getnum ** 2}'