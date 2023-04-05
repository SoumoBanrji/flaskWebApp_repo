from flask import Flask

# initializing flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hijibiji'

    return app