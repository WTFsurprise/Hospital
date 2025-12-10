from typing import List, Optional
from decimal import Decimal
from datetime import datetime, date, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import and_, func, desc
from crud.base import CRUDBase
from models.prescription import Prescription
from schemas.prescription import PrescriptionCreate, PrescriptionUpdate

class CRUDPrescription(CRUDBase[Prescription, PrescriptionCreate, PrescriptionUpdate]):
    def get_by_patient(self, db: Session, patient_id: str, skip: int = 0, limit: int = 100) -> List[Prescription]:
        return (
            db.query(self.model)
            .filter(self.model.patient_id == patient_id)
            .order_by(desc(self.model.created_at))
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_by_medicine(self, db: Session, medicine_id: str, skip: int = 0, limit: int = 100) -> List[Prescription]:
        return (
            db.query(self.model)
            .filter(self.model.medicine_id == medicine_id)
            .order_by(desc(self.model.created_at))
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_by_treatment(self, db: Session, treatment_id: str, skip: int = 0, limit: int = 100) -> List[Prescription]:
        return (
            db.query(self.model)
            .filter(self.model.treatment_id == treatment_id)
            .order_by(desc(self.model.created_at))
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_by_price_range(self, db: Session, min_price: Optional[Decimal] = None, 
                          max_price: Optional[Decimal] = None, skip: int = 0, limit: int = 100) -> List[Prescription]:
        query = db.query(self.model)
        
        if min_price is not None:
            query = query.filter(self.model.price >= float(min_price))
        if max_price is not None:
            query = query.filter(self.model.price <= float(max_price))
        
        return query.order_by(self.model.price).offset(skip).limit(limit).all()
    
    def get_high_price_prescriptions(self, db: Session, threshold: Decimal, skip: int = 0, limit: int = 100) -> List[Prescription]:
        return (
            db.query(self.model)
            .filter(self.model.price >= float(threshold))
            .order_by(desc(self.model.price))
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_by_patient_and_medicine(self, db: Session, patient_id: str, medicine_id: str, skip: int = 0, limit: int = 100) -> List[Prescription]:
        return (
            db.query(self.model)
            .filter(and_(
                self.model.patient_id == patient_id,
                self.model.medicine_id == medicine_id
            ))
            .order_by(desc(self.model.created_at))
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_patient_prescriptions_by_time(self, db: Session, patient_id: str, start_date: Optional[date] = None, 
                                         end_date: Optional[date] = None, skip: int = 0, limit: int = 100) -> List[Prescription]:
        query = db.query(self.model).filter(self.model.patient_id == patient_id)
        
        if start_date:
            query = query.filter(self.model.created_at >= start_date)
        if end_date:
            query = query.filter(self.model.created_at <= end_date)
        
        return query.order_by(desc(self.model.created_at)).offset(skip).limit(limit).all()
    
    def get_recent_prescriptions(self, db: Session, days: int = 7, skip: int = 0, limit: int = 100) -> List[Prescription]:
        cutoff_date = datetime.now() - timedelta(days=days)
        return (
            db.query(self.model)
            .filter(self.model.created_at >= cutoff_date)
            .order_by(desc(self.model.created_at))
            .offset(skip)
            .limit(limit)
            .all()
        )
    
crud_prescription = CRUDPrescription(Prescription)