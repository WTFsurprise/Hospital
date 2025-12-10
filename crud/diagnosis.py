from typing import List, Optional, Any
from datetime import datetime
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.diagnosis import Diagnosis
from schemas.diagnosis import DiagnosisCreate, DiagnosisUpdate


class CRUDDiagnosis(CRUDBase[Diagnosis, DiagnosisCreate, DiagnosisUpdate]):

    def get_by_registration(self, db: Session, registration_id: str) -> Optional[Diagnosis]:
        return (
            db.query(self.model)
            .filter(self.model.registration_id == registration_id)
            .first()
        )

    def get_by_doctor(self, db: Session, doctor_id: str, skip: int = 0, limit: int = 100) -> List[Diagnosis]:
        return (
            db.query(self.model)
            .filter(self.model.doctor_id == doctor_id)
            .order_by(self.model.diagnosis_time.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_patient(self, db: Session, patient_id: str, skip: int = 0, limit: int = 100) -> List[Diagnosis]:
        return (
            db.query(self.model)
            .filter(self.model.patient_id == patient_id)
            .order_by(self.model.diagnosis_time.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_multi_filtered(
            self,
            db: Session,
            registration_id: Optional[str] = None,
            doctor_id: Optional[str] = None,
            patient_id: Optional[str] = None,
            skip: int = 0,
            limit: int = 100,
            sort_by: str = 'diagnosis_time',
            sort_order: str = 'desc'
    ) -> List[Diagnosis]:
        query = db.query(self.model)

        if registration_id:
            query = query.filter(self.model.registration_id == registration_id)
        if doctor_id:
            query = query.filter(self.model.doctor_id == doctor_id)
        if patient_id:
            query = query.filter(self.model.patient_id == patient_id)

        sort_attr = getattr(self.model, sort_by, self.model.created_at)
        if sort_order == 'desc':
            query = query.order_by(sort_attr.desc())
        else:
            query = query.order_by(sort_attr.asc())

        return query.offset(skip).limit(limit).all()

    # 3. 模糊搜索
    def search_by_result(self, db: Session, keyword: str, skip: int = 0, limit: int = 100) -> List[Diagnosis]:
        return (
            db.query(self.model)
            .filter(self.model.diagnosis_result.like(f"%{keyword}%"))
            .offset(skip)
            .limit(limit)
            .all()
        )

    # 4. 时间范围查询
    def get_by_date_range(
            self,
            db: Session,
            start_time: Optional[datetime] = None,
            end_time: Optional[datetime] = None,
            skip: int = 0,
            limit: int = 100
    ) -> List[Diagnosis]:
        query = db.query(self.model)

        if start_time:
            query = query.filter(self.model.diagnosis_time >= start_time)
        if end_time:
            query = query.filter(self.model.diagnosis_time <= end_time)

        return query.order_by(self.model.diagnosis_time.desc()).offset(skip).limit(limit).all()


crud_diagnosis = CRUDDiagnosis(Diagnosis)