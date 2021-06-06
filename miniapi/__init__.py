from flask import Flask, jsonify

__version__ = '0.0.2'


def create_app():

    app = Flask(__name__)

    @app.route("/")
    def hello():
        return jsonify(message="Hello !")

    return app
