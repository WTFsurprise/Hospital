from typing import List,Any,Optional
from decimal import Decimal
from datetime import datetime, date, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import and_, func, desc
from crud.base import CRUDBase
from models.medicine import Medicine
from schemas.medicine import MedicineCreate, MedicineUpdate

class CRUDMedicine(CRUDBase[Medicine, MedicineCreate, MedicineUpdate]):
    def get_by_otc(self, db: Session, is_otc: bool, skip: int = 0, limit: int = 100) -> list[type[Medicine]]:
        return (
            db.query(self.model)
            .filter(self.model.is_otc == is_otc)
            .offset(skip)
            .limit(limit)
            .all()
        )
    def get_by_name(self, db: Session, medicine_name: str) -> List[Medicine]:
        return (
            db.query(self.model)
            .filter(self.model.medicine_name == medicine_name)
            .all()
        )
    
    def search_by_name(self, db: Session, keyword: str, skip: int = 0, limit: int = 100) -> List[Medicine]:
        return (
            db.query(self.model)
            .filter(self.model.medicine_name.like(f"%{keyword}%"))
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_by_price_range(self, db: Session, min_price: Optional[Decimal] = None, 
                          max_price: Optional[Decimal] = None, skip: int = 0, limit: int = 100) -> List[Medicine]:
        query = db.query(self.model)
        
        if min_price is not None:
            query = query.filter(self.model.price >= float(min_price))
        if max_price is not None:
            query = query.filter(self.model.price <= float(max_price))
        
        return query.order_by(self.model.price).offset(skip).limit(limit).all()
    
    def get_high_price_medicines(self, db: Session, threshold: Decimal, skip: int = 0, limit: int = 100) -> List[Medicine]:
        return (
            db.query(self.model)
            .filter(self.model.price >= float(threshold))
            .order_by(self.model.price.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_low_stock(self, db: Session, threshold: int = 10, skip: int = 0, limit: int = 100) -> List[Medicine]:
        return (
            db.query(self.model)
            .filter(self.model.quantity < threshold)
            .order_by(self.model.quantity)
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_by_quantity_range(self, db: Session, min_qty: Optional[int] = None, 
                             max_qty: Optional[int] = None, skip: int = 0, limit: int = 100) -> List[Medicine]:
        query = db.query(self.model)
        
        if min_qty is not None:
            query = query.filter(self.model.quantity >= min_qty)
        if max_qty is not None:
            query = query.filter(self.model.quantity <= max_qty)
        
        return query.order_by(self.model.quantity).offset(skip).limit(limit).all()
    
    def get_expiring_soon(self, db: Session, days: int = 30, skip: int = 0, limit: int = 100) -> List[Medicine]:
        target_date = date.today()
        warning_date = target_date + timedelta(days=days)
        
        return (
            db.query(self.model)
            .filter(and_(
                self.model.expiration_date >= target_date,
                self.model.expiration_date <= warning_date
            ))
            .order_by(self.model.expiration_date)
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_expired(self, db: Session, skip: int = 0, limit: int = 100) -> List[Medicine]:
        return (
            db.query(self.model)
            .filter(self.model.expiration_date < date.today())
            .order_by(self.model.expiration_date)
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_by_production_date_range(self, db: Session, start_date: Optional[date] = None, 
                                    end_date: Optional[date] = None, skip: int = 0, limit: int = 100) -> List[Medicine]:
        query = db.query(self.model)
        
        if start_date is not None:
            query = query.filter(self.model.production_date >= start_date)
        if end_date is not None:
            query = query.filter(self.model.production_date <= end_date)
        
        return query.order_by(self.model.production_date).offset(skip).limit(limit).all()
    
    def get_by_factory(self, db: Session, factory_id: str, skip: int = 0, limit: int = 100) -> List[Medicine]:
        return (
            db.query(self.model)
            .filter(self.model.factory_id == factory_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


crud_medicine = CRUDMedicine(Medicine)