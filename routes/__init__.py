from fastapi import FastAPI

from routes import cam


def register_to(app: FastAPI):
    app.include_router(cam.router)