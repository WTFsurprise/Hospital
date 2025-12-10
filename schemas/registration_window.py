from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class RegistrationWindowBase(BaseModel):
    doctor_id: Optional[str]
    waiting_count: Optional[int] = 0

class RegistrationWindowCreate(RegistrationWindowBase):
    pass

class RegistrationWindowUpdate(RegistrationWindowBase):
    pass

class RegistrationWindow(RegistrationWindowBase):
    window_id: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)