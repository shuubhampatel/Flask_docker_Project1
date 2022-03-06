"""A simple flask web app"""
from flask import Flask, render_template


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    @app.route("/")
    def index():
        return render_template('index.html')

    @app.route("/git")
    def git():
        return render_template('git.html')

    @app.route("/docker")
    def docker():
        return render_template('docker.html')

    @app.route("/flask")
    def flask():
        return render_template('flask.html')

    @app.route("/cicd")
    def cicd():
        return render_template('cicd.html')

    @app.route("/bootstrap")
    def bootstrap():
        return render_template('bootstrap.html')

    return app
