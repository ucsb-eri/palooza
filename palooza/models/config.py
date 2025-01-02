from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy_serializer import SerializerMixin

from palooza import db


class Config(db.Model, SerializerMixin):
    __tablename__ = "configs"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    value: Mapped[str] = mapped_column()

    @classmethod
    def current_palooza(cls):
        current_palooza = Config.query.filter(Config.name == "current_palooza").first()
        return int(current_palooza.value) if current_palooza else None

    def save(self):
        db.session.add(self)
        db.session.commit()

        return self
