from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import and_
from crud.base import CRUDBase
from models.treatment import Treatment
from schemas.treatment import TreatmentCreate, TreatmentUpdate


class CRUDTreatment(CRUDBase[Treatment, TreatmentCreate, TreatmentUpdate]):
    def get_multi_filtered(
            self,
            db: Session,
            diagnosis_id: Optional[str] = None,
            treatment_id: Optional[str] = None,
            doctor_id: Optional[str] = None,  # 注意：ID通常保持类型一致，假设为str
            sort_by: str = 'created_at',
            sort_order: str = 'desc',
            skip: int = 0,
            limit: int = 100
    ) -> List[Treatment]:
        query = db.query(self.model)

        if diagnosis_id:
            query = query.filter(self.model.diagnosis_id == diagnosis_id)
        if treatment_id:
            query = query.filter(self.model.treatment_id == treatment_id)
        if doctor_id:
            query = query.filter(self.model.doctor_id == doctor_id)

        # 原代码中 "if diagnosis_id and doctor_id" 的逻辑在上面三个独立if中已经涵盖了。
        # SQLAlchemy 会自动将多个 filter 连接为 AND 关系，所以不需要显式写 and_() 除非是在同一个 filter() 调用内部。

        # 排序处理
        # getattr(self.model, ...) 确保是对 Treatment 模型进行操作
        sort_attr = getattr(self.model, sort_by, self.model.created_at)

        if sort_order == 'desc':
            query = query.order_by(sort_attr.desc())
        else:
            query = query.order_by(sort_attr.asc())

        return query.offset(skip).limit(limit).all()


crud_treatment = CRUDTreatment(Treatment)