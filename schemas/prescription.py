from pydantic import BaseModel, ConfigDict
from datetime import datetime
from decimal import Decimal
from typing import Optional

class PrescriptionBase(BaseModel):
    treatment_id: str
    medicine_id: str
    patient_id: str
    price: Decimal
    quantity: int

class PrescriptionCreate(PrescriptionBase):
    pass

class PrescriptionUpdate(PrescriptionBase):
    pass

class Prescription(PrescriptionBase):
    prescription_id: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)