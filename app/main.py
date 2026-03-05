from fastapi import FastAPI
from app.utils.settings import settings
from app.utils.db import engine, Base
from app.user.router import user_routes
from app.document.router import document_routes

Base.metadata.create_all(engine)

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": f"{settings.APP_NAME} is running in {settings.ENV} environment."}

app.include_router(user_routes)
app.include_router(document_routes)