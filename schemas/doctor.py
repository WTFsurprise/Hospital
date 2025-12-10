from pydantic import BaseModel, ConfigDict
from datetime import datetime
from decimal import Decimal
from typing import Optional
from enum import Enum

class GenderEnum(str, Enum):
    M = 'M'
    F = 'F'

class DoctorBase(BaseModel):
    doctor_name: str
    title: str
    gender: GenderEnum
    age: int
    experience: Optional[int] = 0
    salary: Optional[Decimal] = 0.00
    dept_id: Optional[str] = None

class DoctorCreate(DoctorBase):
    pass

class DoctorUpdate(DoctorBase):
    pass

class Doctor(DoctorBase):
    doctor_id: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)