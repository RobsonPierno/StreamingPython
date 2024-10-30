from sqlalchemy import Column, Integer, Boolean, Date
from app.db.base import Base

class History(Base):
    __tablename__ = "netflix"
    __table_args__ = {'schema': 'streaming'}

    id_pessoa = Column("idpessoa", Integer, primary_key=True, index=True)
    id_filme = Column("idfilme", Integer, primary_key=True, index=True)
    liked = Column("gostou", Boolean)
    dt_play = Column("dtplay", Date)
    finished = Column("terminou", Boolean)
