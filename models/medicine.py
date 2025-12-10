from sqlalchemy import Column, String, Integer, DateTime, DECIMAL, Date, Boolean, Text, ForeignKey, func
from database import Base

class Medicine(Base):
    __tablename__ = "medicine"
    medicine_id = Column(String(18), primary_key=True)
    medicine_name = Column(String(100), nullable=False)
    quantity = Column(Integer, default=0)
    is_otc = Column(Boolean, default=0)
    production_date = Column(Date, nullable=False)
    expiration_date = Column(Date, nullable=False)
    indications = Column(Text)
    price = Column(DECIMAL(10, 2), default=0.00)
    factory_id = Column(String(18), ForeignKey("pharmaceutical_factory.factory_id"))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())