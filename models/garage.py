from sqlalchemy import Column, String, Boolean, DateTime, func
from database import Base

class Garage(Base):
    __tablename__ = "garage"
    
    garage_id = Column(String(18), primary_key=True, comment="车库编号")
    is_full = Column(Boolean, default=False, comment="是否满位")
    area = Column(String(10), nullable=True, comment="车库区域")
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())