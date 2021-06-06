from flask import Flask

__version__ = '0.0.1'


def create_app():

    app = Flask(__name__)

    @app.route("/")
    def hello():
        return {"message": "Hello !"}

    return app
