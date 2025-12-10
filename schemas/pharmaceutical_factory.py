from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class PharmaceuticalFactoryBase(BaseModel):
    factory_name: str
    manager: str
    address: str
    qualification_level: int
    phone_number: str

class PharmaceuticalFactoryCreate(PharmaceuticalFactoryBase):
    pass

class PharmaceuticalFactoryUpdate(PharmaceuticalFactoryBase):
    pass

class PharmaceuticalFactory(PharmaceuticalFactoryBase):
    factory_id: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)