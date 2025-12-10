from crud.base import CRUDBase
from models.garage import Garage
from schemas.garage import GarageCreate, GarageUpdate
from sqlalchemy.orm import Session
class CRUDGarage(CRUDBase[Garage, GarageCreate, GarageUpdate]):
    def get_by_garage_id(self, db: Session, garage_id: str):
        return db.query(Garage).filter(Garage.garage_id == garage_id).first()

    def get_available_garages(self, db: Session):
        return db.query(Garage).filter(Garage.is_full == False).order_by(Garage.garage_id).all()


crud_garage = CRUDGarage(Garage)