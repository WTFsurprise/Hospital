from sqlalchemy import Column, String, Integer, DateTime, func
from database import Base

class PharmaceuticalFactory(Base):
    __tablename__ = "pharmaceutical_factory"
    factory_id = Column(String(18), primary_key=True)
    factory_name = Column(String(100), nullable=False)
    manager = Column(String(50), nullable=False)
    address = Column(String(200), nullable=False)
    qualification_level = Column(Integer, nullable=False)
    phone_number = Column(String(20), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())