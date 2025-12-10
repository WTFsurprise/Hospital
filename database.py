from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# 数据库配置
DATABASE_URL = "mysql+pymysql://root:root@192.168.5.20:3306/hospital"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# 依赖注入
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()