from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class TreatmentBase(BaseModel):
    diagnosis_id: str
    doctor_id: str
    treatment_method: Optional[str]
    treatment_time: datetime
    treatment_period: Optional[int]

class TreatmentCreate(TreatmentBase):
    pass

class TreatmentUpdate(TreatmentBase):
    pass

class Treatment(TreatmentBase):
    treatment_id: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)