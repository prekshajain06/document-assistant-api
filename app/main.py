from fastapi import FastAPI
from core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": f"{settings.APP_NAME} is running in {settings.ENV} environment."}