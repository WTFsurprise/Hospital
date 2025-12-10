from typing import Optional

from crud.base import CRUDBase
from database import get_db
from models.department import Department
from schemas.department import DepartmentCreate, DepartmentUpdate
from fastapi import FastAPI,Query,Depends,HTTPException,status
from sqlalchemy.orm import Session

class CRUDDepartment(CRUDBase[Department, DepartmentCreate, DepartmentUpdate]):

    def get_dept(self,dept_id:Optional[str] =Query(None,description="Selected by department_id"),
                 dept_name:Optional[str]=Query(None,description="Selected by department_name"),
                 location:Optional[str]=Query(None,description="Selected by location"),
                 db: Session = Depends(get_db),):#索引查询,在dept_id和dept_name上建立两个索引
        query = db.query(Department)
        if dept_id:#根据部门编号查询
            query = query.filter(Department.department_id == dept_id)
        if dept_name:#根据部门名称查询
            query = query.filter(Department.department_name == dept_name)
        if location:#查询某一特定楼层存在的部门
            filters.append(Department.location.ilike(f"%{location}%"))
        if filters:query = query.filter(*filters)
        dept=query.offset(limit).limit(limit).all()
        return dept



crud_department = CRUDDepartment(Department)