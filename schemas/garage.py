from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class GarageBase(BaseModel):
    is_full: bool = False
    area: Optional[str] = None

class GarageCreate(GarageBase):
    pass

class GarageUpdate(GarageBase):
    pass

class Garage(GarageBase):
    garage_id: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)