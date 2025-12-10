from sqlalchemy import Column, String, Integer, DateTime, DECIMAL, ForeignKey, func
from database import Base

class Prescription(Base):
    __tablename__ = "prescription"
    prescription_id = Column(String(18), primary_key=True)
    treatment_id = Column(String(18), ForeignKey("treatment.treatment_id"))
    medicine_id = Column(String(18), ForeignKey("medicine.medicine_id"))
    patient_id = Column(String(18), ForeignKey("patient.patient_id"))
    price = Column(DECIMAL(10, 2), default=0.00)
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())