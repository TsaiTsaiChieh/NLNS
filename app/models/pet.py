from app.db.base_class import Base
from sqlalchemy import (
    JSON,
    Boolean,
    Column,
    Enum,
    ForeignKey,
    Integer,
    Sequence,
    SmallInteger,
    String,
)
from sqlalchemy.orm import relation


class Pet(Base):
    pet_id_seq = Sequence("pet_id_seq")
    id = Column(
        Integer, pet_id_seq, server_default=pet_id_seq.next_value(), primary_key=True
    )
    name = Column(String(128), comment="寵物名")
    ref = Column(
        Enum("gov", "map", "own", name="ref_types"), nullable=False, comment="資料來源"
    )
    area_id = Column(
        Integer,
        ForeignKey("area.id"),
        nullable=False,
        index=True,
        comment="所屬縣市代碼：2 臺北市 / 3 新北市 / 4 基隆市 / 5 宜蘭縣 / 6 桃園縣 / 7 新竹縣 / 8 新竹市 / 9 苗栗縣 / 10 臺中市 / 11 彰化縣 / 12 南投縣 / 13 雲林縣 / 14 嘉義縣 / 15 嘉義市 / 16 臺南市 / 17 高雄市 / 18 屏東縣 / 19 花蓮縣 / 20 臺東縣 / 21 澎湖縣 / 22 金門縣 / 23 連江縣",
    )
    area = relation("Area", back_populates="pets")
    kind = Column(String(16), nullable=False, index=True, comment="寵物種類")
    sex = Column(
        SmallInteger,
        default=-1,
        nullable=False,
        index=True,
        comment="-1 未知 / 0 母 / 1 公",
    )
    color = Column(String(8))
    age = Column(
        SmallInteger,
        nullable=False,
        default=-1,
        index=True,
        comment="年齡：-1 未知 / 0 幼體 / 1 成體",
    )
    ligation = Column(
        SmallInteger,
        nullable=False,
        default=-1,
        index=True,
        comment="-1 / 未知 / 0 未結紮 / 1 已結紮",
    )
    rabies = Column(
        SmallInteger, nullable=False, default=-1, comment="狂犬病疫苗：-1 未知 / 0 未施打 / 1 已施打"
    )
    found_place = Column(String, comment="尋獲地")
    title = Column(String, comment="寵物文章標題")
    status = Column(
        SmallInteger,
        nullable=False,
        default=0,
        index=True,
        comment="寵物狀態：0 無 / 1 開放 / 2 已被認養 / 3 其他 / -1 死亡",
    )
    remark = Column(String, comment="資料備註")
    address = Column(String)
    phone = Column(String(16))
    image = Column(JSON)