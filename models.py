from datetime import datetime
from sqlalchemy import Column, Integer, Text, DateTime

from database.database import Base


class FAQ(Base):
    __tablename__ = 'faq'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    status = Column(Integer, default=1, comment='노출 여부')
    question = Column(Text, comment='질문')
    answer = Column(Text, comment='대답')
    history = Column(Text, comment='')
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
