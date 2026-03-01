from sqlalchemy import Column, Integer, String, DateTime, Boolean
from app.utils.db import Base

class UserModel(Base):
    __tablename__ = "user_table"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String, nullable=False)
    email = Column(String)
    hashed_password = Column(String, nullable=False)
    