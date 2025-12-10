from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class DepartmentBase(BaseModel):
    dept_name: str
    location: str
    staff_count: Optional[int] = 0

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentUpdate(DepartmentBase):
    pass

class Department(DepartmentBase):
    dept_id: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)