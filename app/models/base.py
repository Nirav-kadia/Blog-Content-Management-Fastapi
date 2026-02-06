from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, DateTime, func, Boolean

#Every table automatically gets below fields 

class Base(DeclarativeBase):
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_deleted = Column(Boolean, default=False)
