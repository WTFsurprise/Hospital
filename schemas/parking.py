from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from decimal import Decimal

class ParkingBase(BaseModel):
    car_no: str
    garage_id: str
    patient_id: Optional[str] = None
    in_time: datetime
    out_time: Optional[datetime] = None
    fee: Optional[Decimal] = None
    car_type: Optional[str] = None

class ParkingCreate(ParkingBase):
    pass

class ParkingUpdate(ParkingBase):
    pass

class Parking(ParkingBase):
    parking_id: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)