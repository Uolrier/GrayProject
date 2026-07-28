from fastapi import FastAPI


app = FastAPI(
    title="GrayProject API",
    description="Personal AI Operating System Backend",
    version="0.1.0"
)


@app.get("/")
def index():
    return {
        "project": "GrayProject",
        "status": "backend running"
    }