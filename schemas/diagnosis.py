from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class DiagnosisBase(BaseModel):
    registration_id: str
    doctor_id: str
    diagnosis_time: datetime
    diagnosis_note: Optional[str]

class DiagnosisCreate(DiagnosisBase):
    pass

class DiagnosisUpdate(DiagnosisBase):
    pass

class Diagnosis(DiagnosisBase):
    diagnosis_id: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)