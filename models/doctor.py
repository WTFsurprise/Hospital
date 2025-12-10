from sqlalchemy import Column, String, Integer, DateTime, DECIMAL, Enum, ForeignKey, func
from database import Base

class Doctor(Base):
    __tablename__ = "doctor"
    doctor_id = Column(String(18), primary_key=True)
    doctor_name = Column(String(20), nullable=False)
    title = Column(String(20), nullable=False)
    gender = Column(Enum('M', 'F'), nullable=False)
    age = Column(Integer, nullable=False)
    experience = Column(Integer, default=0)
    salary = Column(DECIMAL(10, 2), default=0.00)
    dept_id = Column(String(18), ForeignKey("department.dept_id"))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())