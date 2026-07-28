from flask import Flask

from config import settings



def create_app():

    app = Flask(__name__)


    @app.route("/")
    def index():

        return {
            "project": settings.PROJECT_NAME,
            "environment": settings.ENVIRONMENT
        }


    return app