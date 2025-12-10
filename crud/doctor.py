from typing import Optional, List, Any
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.doctor import Doctor
from schemas.doctor import DoctorCreate, DoctorUpdate


class CRUDDoctor(CRUDBase[Doctor, DoctorCreate, DoctorUpdate]):
    def get_multi_filtered(
            self,
            db: Session,
            doctor_id: Optional[str] = None,
            dept_id: Optional[str] = None,
            min_age: Optional[int] = None,
            max_age: Optional[int] = None,
            min_salary: Optional[float] = None,  # 重命名更清晰，通常是查询大于某薪资
            sort_by: str = 'created_at',
            sort_order: str = 'desc',
            skip: int = 0,
            limit: int = 100
    ) -> List[Doctor]:
        query = db.query(self.model)

        if doctor_id:
            query = query.filter(self.model.doctor_id == doctor_id)
        if dept_id:
            query = query.filter(self.model.dept_id == dept_id)
        if min_age is not None:
            query = query.filter(self.model.age >= min_age)
        if max_age is not None:
            query = query.filter(self.model.age <= max_age)
        if min_salary is not None:
            query = query.filter(self.model.salary >= min_salary)

        # 排序处理
        # getattr 获取模型属性，如果字段不存在默认使用 created_at
        sort_attr = getattr(self.model, sort_by, self.model.created_at)

        if sort_order == 'desc':
            query = query.order_by(sort_attr.desc())
        else:
            query = query.order_by(sort_attr.asc())

        return query.offset(skip).limit(limit).all()


# 实例化对象
crud_doctor = CRUDDoctor(Doctor)