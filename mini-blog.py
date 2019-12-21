from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/sign_up')
def sign_up():
    return "sign_up"


@app.route('/sign_in')
def sign_in():
    return "sign_in"


@app.route('/u/<user_id>')
def u(user_id: str):
    return user_id





if __name__ == '__main__':
    app.run()
