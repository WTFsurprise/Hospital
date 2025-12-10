from sqlalchemy import Column, String, DateTime, DECIMAL, ForeignKey, func
from database import Base

class Registration(Base):
    __tablename__ = "registration"
    registration_id = Column(String(18), primary_key=True)
    window_id = Column(String(18), ForeignKey("registration_window.window_id"))
    patient_id = Column(String(18), ForeignKey("patient.patient_id"))
    doctor_id = Column(String(18), ForeignKey("doctor.doctor_id"))
    registration_time = Column(DateTime, nullable=False)
    fee = Column(DECIMAL(10, 2), default=0.00)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())