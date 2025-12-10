from sqlalchemy import Column, String, DateTime, Text, ForeignKey, func
from database import Base

class Diagnosis(Base):
    __tablename__ = "diagnosis"
    diagnosis_id = Column(String(18), primary_key=True)
    registration_id = Column(String(18), ForeignKey("registration.registration_id"))
    doctor_id = Column(String(18), ForeignKey("doctor.doctor_id"))
    diagnosis_time = Column(DateTime, nullable=False)
    diagnosis_note = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
