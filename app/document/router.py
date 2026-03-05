from fastapi import APIRouter, Depends, Request, File, UploadFile
from sqlalchemy.orm import Session
from app.document.dtos import DocumentResponseSchema
from app.utils.db import get_db
from app.user import controller as user_controller
from app.document import controller

document_routes = APIRouter(prefix="/document")

@document_routes.post("/upload", response_model=DocumentResponseSchema)
async def upload_document(request: Request, file: UploadFile = File(...), db: Session = Depends(get_db)):
    user = user_controller.is_authenticated(request, db)
    return await controller.upload_document(file, user, db)

@document_routes.get("/list")
def list_documents(request: Request, db: Session = Depends(get_db)):
    user = user_controller.is_authenticated(request, db)
    return controller.list_documents(user, db)

