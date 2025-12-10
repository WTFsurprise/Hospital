from sqlalchemy import Column, String, Integer, DateTime, func
from database import Base

class Department(Base):
    __tablename__ = "department"
    dept_id = Column(String(18), primary_key=True)
    dept_name = Column(String(20), nullable=False)
    location = Column(String(20), nullable=False)
    staff_count = Column(Integer, default=0)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())