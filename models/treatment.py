from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, func
from database import Base

class Treatment(Base):
    __tablename__ = "treatment"
    treatment_id = Column(String(18), primary_key=True)
    diagnosis_id = Column(String(18), ForeignKey("diagnosis.diagnosis_id"))
    doctor_id = Column(String(18), ForeignKey("doctor.doctor_id"))
    treatment_method = Column(String(50))
    treatment_time = Column(DateTime, nullable=False)
    treatment_period = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())