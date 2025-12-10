from typing import List, Optional
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.registration import Registration
from schemas.registration import RegistrationCreate, RegistrationUpdate


class CRUDRegistration(CRUDBase[Registration, RegistrationCreate, RegistrationUpdate]):
    def get_multi_filtered(
            self,
            db: Session,
            registration_id: Optional[str] = None,
            doctor_id: Optional[str] = None,
            window_id: Optional[str] = None,
            patient_id: Optional[str] = None,
            sort_by: str = 'created_at',
            sort_order: str = 'desc',
            skip: int = 0,
            limit: int = 100
    ) -> List[Registration]:
        query = db.query(self.model)

        if registration_id:
            # 假设模型中的主键字段名为 id
            query = query.filter(self.model.id == registration_id)
        if doctor_id:
            query = query.filter(self.model.doctor_id == doctor_id)
        if window_id:
            query = query.filter(self.model.window_id == window_id)
        if patient_id:
            query = query.filter(self.model.patient_id == patient_id)

        # 排序处理
        # 如果字段不存在，默认按 created_at 排序
        sort_attr = getattr(self.model, sort_by, self.model.created_at)

        if sort_order == 'desc':
            query = query.order_by(sort_attr.desc())
        else:
            query = query.order_by(sort_attr.asc())

        return query.offset(skip).limit(limit).all()


crud_registration = CRUDRegistration(Registration)