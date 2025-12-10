from typing import List, Optional, Dict, Any
from datetime import datetime, date, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, func, desc, asc
from crud.base import CRUDBase
from models.stock_warning import StockWarning
from schemas.stock_warning import StockWarningCreate, StockWarningUpdate, WarningTypeEnum

class CRUDStockWarning(CRUDBase[StockWarning, StockWarningCreate, StockWarningUpdate]):
    def get_by_medicine(self, db: Session, medicine_id: str, skip: int = 0, limit: int = 100) -> List[StockWarning]:
        return (
            db.query(self.model)
            .filter(self.model.medicine_id == medicine_id)
            .order_by(desc(self.model.warning_time))
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_by_warning_type(self, db: Session, warning_type: WarningTypeEnum, skip: int = 0, limit: int = 100) -> List[StockWarning]:
        return (
            db.query(self.model)
            .filter(self.model.warning_type == warning_type.value)
            .order_by(desc(self.model.warning_time))
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_unhandled_warnings(self, db: Session, skip: int = 0, limit: int = 100) -> List[StockWarning]:
        return (
            db.query(self.model)
            .filter(self.model.is_handled == False)
            .order_by(desc(self.model.warning_time))
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_handled_warnings(self, db: Session, skip: int = 0, limit: int = 100) -> List[StockWarning]:
        return (
            db.query(self.model)
            .filter(self.model.is_handled == True)
            .order_by(desc(self.model.handled_at))
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_by_time_status(self, db: Session, is_handled: Optional[bool] = None, 
                          start_date: Optional[date] = None, end_date: Optional[date] = None,
                          skip: int = 0, limit: int = 100) -> List[StockWarning]:
        query = db.query(self.model)
        
        if is_handled is not None:
            query = query.filter(self.model.is_handled == is_handled)
        
        if start_date:
            query = query.filter(self.model.warning_time >= start_date)
        if end_date:
            query = query.filter(self.model.warning_time <= end_date)
        
        return query.order_by(desc(self.model.warning_time)).offset(skip).limit(limit).all()
    
    def get_recent_warnings(self, db: Session, days: int = 7, skip: int = 0, limit: int = 100) -> List[StockWarning]:
        cutoff_date = datetime.now() - timedelta(days=days)
        return (
            db.query(self.model)
            .filter(self.model.warning_time >= cutoff_date)
            .order_by(desc(self.model.warning_time))
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_by_medicine_and_time(self, db: Session, medicine_id: str, 
                                start_date: Optional[date] = None, end_date: Optional[date] = None,
                                skip: int = 0, limit: int = 100) -> List[StockWarning]:
        query = db.query(self.model).filter(self.model.medicine_id == medicine_id)
        
        if start_date:
            query = query.filter(self.model.warning_time >= start_date)
        if end_date:
            query = query.filter(self.model.warning_time <= end_date)
        
        return query.order_by(desc(self.model.warning_time)).offset(skip).limit(limit).all()
    
    def get_low_stock_warnings(self, db: Session, skip: int = 0, limit: int = 100) -> List[StockWarning]:
        return (
            db.query(self.model)
            .filter(self.model.warning_type == WarningTypeEnum.LOW_STOCK.value)
            .order_by(desc(self.model.warning_time))
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_near_expiration_warnings(self, db: Session, skip: int = 0, limit: int = 100) -> List[StockWarning]:
        return (
            db.query(self.model)
            .filter(self.model.warning_type == WarningTypeEnum.NEAR_EXPIRATION.value)
            .order_by(desc(self.model.warning_time))
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_warning_statistics(self, db: Session) -> Dict[str, Any]:
        # 按类型统计
        type_stats = (
            db.query(
                self.model.warning_type,
                func.count(self.model.warning_id).label('count'),
                func.sum(func.if_(self.model.is_handled == True, 1, 0)).label('handled_count')
            )
            .group_by(self.model.warning_type)
            .all()
        )
        
        # 按处理状态统计
        handled_stats = (
            db.query(
                self.model.is_handled,
                func.count(self.model.warning_id).label('count')
            )
            .group_by(self.model.is_handled)
            .all()
        )
        
        # 最近24小时预警数
        last_24h = datetime.now() - timedelta(hours=24)
        recent_count = (
            db.query(func.count(self.model.warning_id))
            .filter(self.model.warning_time >= last_24h)
            .scalar()
        ) or 0
        
        # 未处理预警的药品分布
        unhandled_by_medicine = (
            db.query(
                self.model.medicine_id,
                self.model.medicine_name,
                func.count(self.model.warning_id).label('warning_count')
            )
            .filter(self.model.is_handled == False)
            .group_by(self.model.medicine_id, self.model.medicine_name)
            .order_by(desc(func.count(self.model.warning_id)))
            .limit(10)
            .all()
        )
        
        return {
            'total_warnings': db.query(func.count(self.model.warning_id)).scalar() or 0,
            'recent_24h_warnings': recent_count,
            'type_distribution': {
                stat.warning_type: {
                    'total': stat.count,
                    'handled': stat.handled_count,
                    'unhandled': stat.count - stat.handled_count
                }
                for stat in type_stats
            },
            'handled_status': {
                'handled': next((stat.count for stat in handled_stats if stat.is_handled), 0),
                'unhandled': next((stat.count for stat in handled_stats if not stat.is_handled), 0)
            },
            'top_unhandled_medicines': [
                {
                    'medicine_id': stat.medicine_id,
                    'medicine_name': stat.medicine_name,
                    'warning_count': stat.warning_count
                }
                for stat in unhandled_by_medicine
            ]
        }
    
    def mark_as_handled(self, db: Session, warning_id: str, handled_by: str) -> Optional[StockWarning]:
        warning = db.query(self.model).filter(self.model.warning_id == warning_id).first()
        if warning and not warning.is_handled:
            warning.is_handled = True
            warning.handled_by = handled_by
            warning.handled_at = datetime.now()
            db.commit()
            db.refresh(warning)
        return warning

crud_stock_warning = CRUDStockWarning(StockWarning)