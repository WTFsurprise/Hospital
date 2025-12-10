from pydantic import BaseModel, ConfigDict
from datetime import datetime
from enum import Enum
from typing import Optional

class WarningTypeEnum(str, Enum):
    LOW_STOCK = 'LOW_STOCK'
    NEAR_EXPIRATION = 'NEAR_EXPIRATION'

class StockWarningBase(BaseModel):
    medicine_id: str
    medicine_name: str
    current_quantity: int
    warning_type: WarningTypeEnum
    warning_message: Optional[str]
    warning_time: datetime
    is_handled: bool = False
    handled_by: Optional[str]
    handled_at: Optional[datetime]

class StockWarningCreate(StockWarningBase):
    pass

class StockWarningUpdate(StockWarningBase):
    pass

class StockWarning(StockWarningBase):
    warning_id: str
    created_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)