# from flask import Flask, jsonify, request
# from werkzeug.exceptions import HTTPException

# from app.core.logger import logger


# def create_app():
#     app = Flask(__name__)

#     logger.info("Flask application initialized")

#     @app.errorhandler(Exception)
#     def handle_exception(error):
#         if isinstance(error, HTTPException):
#             return error

#         logger.exception("Unhandled exception: %s %s", request.method, request.path)

#         return jsonify({"code": 500, "message": "Internal Server Error"}), 500

#     @app.route("/")
#     def index():
#         logger.info("Index endpoint accessed")

#         return {"project": "GrayProject", "status": "running"}

#     return app

"""
GrayProject backend application package.
"""
