from pydantic import BaseModel, ConfigDict
from datetime import datetime
from decimal import Decimal
from typing import Optional

class RegistrationBase(BaseModel):
    window_id: Optional[str]
    patient_id: str
    doctor_id: str
    registration_time: datetime
    fee: Decimal

class RegistrationCreate(RegistrationBase):
    pass

class RegistrationUpdate(BaseModel):
    window_id: Optional[str] = None
    patient_id: Optional[str] = None
    doctor_id: Optional[str] = None
    fee: Optional[Decimal] = None

class Registration(RegistrationBase):
    registration_id: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)