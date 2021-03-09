from app.db.base_class import Base
from sqlalchemy import Column, Integer, Sequence, SmallInteger, String

# from sqlalchemy.orm import relation


class Area(Base):
    area_id_seq = Sequence("area_id_seq")
    id = Column(
        Integer, area_id_seq, server_default=area_id_seq.next_value(), primary_key=True
    )
    # pet = relation("Pet", back_populates="area")
    name = Column(String(8), nullable=False)
