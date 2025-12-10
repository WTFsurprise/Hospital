from pydantic import BaseModel, ConfigDict
from datetime import datetime
from decimal import Decimal
from typing import Optional
from enum import Enum

class GenderEnum(str, Enum):
    M = 'M'
    F = 'F'

class PatientBase(BaseModel):
    patient_name: str
    age: int
    gender: GenderEnum
    height: Optional[Decimal]
    weight: Optional[Decimal]

class PatientCreate(PatientBase):
    pass

class PatientUpdate(PatientBase):
    pass

class Patient(PatientBase):
    patient_id: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)