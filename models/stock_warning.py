from sqlalchemy import Column, String, Integer, DateTime, Enum, Boolean, ForeignKey, func
from database import Base

class StockWarning(Base):
    __tablename__ = "stock_warning"
    warning_id = Column(String(18), primary_key=True)
    medicine_id = Column(String(18), ForeignKey("medicine.medicine_id"))
    medicine_name = Column(String(100), nullable=False)
    current_quantity = Column(Integer, nullable=False)
    warning_type = Column(Enum('LOW_STOCK','NEAR_EXPIRATION'), default='LOW_STOCK')
    warning_message = Column(String(200))
    warning_time = Column(DateTime, nullable=False)
    is_handled = Column(Boolean, default=0)
    handled_by = Column(String(50))
    handled_at = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())