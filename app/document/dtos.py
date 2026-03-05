from pydantic import BaseModel

class DocumentResponseSchema(BaseModel):
    doc_id: int
    filename: str
    user_id: int

    class Config:
        from_attributes = True