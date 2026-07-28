from flask import Flask

from app.utils.logger import setup_logger



def create_app():

    app = Flask(__name__)


    setup_logger(app)



    @app.route("/")
    def index():

        app.logger.info(
            "Index endpoint accessed"
        )

        return {
            "project": "GrayProject",
            "status": "running"
        }


    return app