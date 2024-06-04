from core.config import settings
from fastapi import FastAPI


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    return app


app = start_application()


@app.get("/")
def hello():
    return {"message": "Hello World"}
