from sqlalchemy import Column, Integer, String, DateTime, DECIMAL, ForeignKey, func
from database import Base

class Parking(Base):
    __tablename__ = "parking"
    
    parking_id = Column(String(18), primary_key=True, comment="停车记录ID")
    car_no = Column(String(20), nullable=False, comment="车牌号")
    garage_id = Column(String(18), ForeignKey("garage.garage_id"), nullable=False, comment="关联车库编号")
    patient_id = Column(String(18), ForeignKey("patient.patient_id"), nullable=True, comment="关联患者编号")
    in_time = Column(DateTime, nullable=False, comment="入场时间")
    out_time = Column(DateTime, nullable=True, comment="出场时间")
    fee = Column(DECIMAL(10, 2), nullable=True, comment="停车费用")
    car_type = Column(String(10), nullable=True, comment="车辆类型")
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())