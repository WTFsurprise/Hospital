from pydantic import BaseModel, ConfigDict
from datetime import date, datetime
from decimal import Decimal
from typing import Optional

class MedicineBase(BaseModel):
    medicine_name: str
    quantity: int
    is_otc: bool
    production_date: date
    expiration_date: date
    indications: Optional[str]
    price: Decimal
    factory_id: Optional[str]

class MedicineCreate(MedicineBase):
    pass

class MedicineUpdate(MedicineBase):
    pass

class Medicine(MedicineBase):
    medicine_id: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)