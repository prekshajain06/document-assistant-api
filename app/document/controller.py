import os
import uuid
from app.utils import db
from app.utils.settings import settings
from fastapi import UploadFile, HTTPException, status
from sqlalchemy.orm import Session
from app.document.models import DocumentModel

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UPLOAD_DIR = os.path.join(BASE_DIR, settings.UPLOAD_FOLDER)

os.makedirs(UPLOAD_DIR, exist_ok=True)

async def upload_document(file: UploadFile, user, db: Session):

    # if not file:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No file uploaded.")
    
    if not file.filename:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No file selected")

    content = await file.read()
    if not content:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Empty file uploaded")

    unique_name = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, unique_name)
    
    # Save file to local
    with open(file_path, "wb") as f:
        # content = await file.read()
        f.write(content)
    
    new_document = DocumentModel(
        filename=file.filename,
        filepath=file_path,
        user_id=user.id
    )
    db.add(new_document)
    db.commit()
    db.refresh(new_document)

    return new_document

def list_documents(user, db: Session):
    documents = db.query(DocumentModel).filter(DocumentModel.user_id == user.id).all()
    return documents