from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, func
from database import Base

class RegistrationWindow(Base):
    __tablename__ = "registration_window"
    window_id = Column(String(18), primary_key=True)
    doctor_id = Column(String(18), ForeignKey("doctor.doctor_id"))
    waiting_count = Column(Integer, default=0)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())