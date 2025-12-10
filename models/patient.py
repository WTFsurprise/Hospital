from sqlalchemy import Column, String, Integer, DateTime, DECIMAL, Enum, func
from database import Base

class Patient(Base):
    __tablename__ = "patient"
    patient_id = Column(String(18), primary_key=True)
    patient_name = Column(String(20), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(Enum('M', 'F'), nullable=False)
    height = Column(DECIMAL(5, 2))
    weight = Column(DECIMAL(5, 2))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
