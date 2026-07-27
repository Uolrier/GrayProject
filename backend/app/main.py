from flask import Flask


def create_app():
    """
    创建 Flask 应用实例

    后续所有 Atlas 后端模块都会挂载到这里。
    """

    app = Flask(__name__)

    @app.route("/")
    def index():
        return {
            "project": "Project Atlas",
            "status": "backend running"
        }

    return app


if __name__ == "__main__":
    app = create_app()

    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )