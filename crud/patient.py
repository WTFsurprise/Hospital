from typing import List, Optional
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.patient import Patient
from schemas.patient import PatientCreate, PatientUpdate


class CRUDPatient(CRUDBase[Patient, PatientCreate, PatientUpdate]):

    def get_multi_filtered(
            self,
            db: Session,
            patient_id: Optional[str] = None,
            age: Optional[int] = None,
            sort_by: str = 'created_at',
            sort_order: str = 'desc',
            skip: int = 0,
            limit: int = 100
    ) -> List[Patient]:
        query = db.query(self.model)

        # 过滤条件
        if patient_id:
            query = query.filter(self.model.patient_id == patient_id)
        if age is not None:  # 使用 is not None 以允许查询 0 岁
            query = query.filter(self.model.age == age)

        # 排序逻辑
        # 只有当模型中有这个字段时才排序，否则默认按 created_at (如果存在) 或不排序
        if hasattr(self.model, sort_by):
            sort_attr = getattr(self.model, sort_by)
            if sort_order == 'desc':
                query = query.order_by(sort_attr.desc())
            else:
                query = query.order_by(sort_attr.asc())

        return query.offset(skip).limit(limit).all()


crud_patient = CRUDPatient(Patient)