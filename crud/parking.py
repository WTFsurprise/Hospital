from crud.base import CRUDBase
from models.parking import Parking
from schemas.parking import ParkingCreate, ParkingUpdate
from sqlalchemy.orm import Session  # 新增：导入数据库会话对象

class CRUDParking(CRUDBase[Parking, ParkingCreate, ParkingUpdate]):
    def get_by_garage_id(self, db: Session, garage_id: str):
        return db.query(Parking).filter(Parking.garage_id == garage_id).order_by(Parking.in_time.desc()).all()

    def get_by_patient_id(self, db: Session, patient_id: str):
        return db.query(Parking).filter(Parking.patient_id == patient_id).order_by(Parking.in_time.desc()).all()

crud_parking = CRUDParking(Parking)