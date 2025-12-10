from typing import List, Optional
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.registration_window import RegistrationWindow
from schemas.registration_window import RegistrationWindowCreate, RegistrationWindowUpdate


class CRUDRegistrationWindow(CRUDBase[RegistrationWindow, RegistrationWindowCreate, RegistrationWindowUpdate]):

    def get_multi_filtered(
            self,
            db: Session,
            window_id: Optional[str] = None,
            doctor_id: Optional[int] = None,
            skip: int = 0,
            limit: int = 100
    ) -> List[RegistrationWindow]:
        query = db.query(self.model)

        if window_id:
            # 假设模型的主键或对应字段是 id
            query = query.filter(self.model.id == window_id)

        if doctor_id:
            query = query.filter(self.model.doctor_id == doctor_id)

        return query.offset(skip).limit(limit).all()


# 实例化
crud_registration_window = CRUDRegistrationWindow(RegistrationWindow)