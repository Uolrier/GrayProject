from flask import Flask

from app.core.logger import logger


def create_app():

    app = Flask(__name__)


    logger.info(
        "GrayProject Flask application initialized"
    )


    @app.route("/")
    def index():

        logger.info(
            "Root endpoint accessed"
        )

        return {
            "project": "GrayProject",
            "status": "running"
        }


    return app