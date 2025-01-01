from dataclasses import dataclass
from typing import List, Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_serializer import SerializerMixin

from palooza import db
from palooza.models.node import Node


class Palooza(db.Model, SerializerMixin):
    __tablename__ = "paloozas"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[Optional[str]]
    nodes: Mapped[List["Node"]] = relationship(back_populates="palooza")

    @classmethod
    def find_by_name(cls, name):
        return Palooza.query.filter(Palooza.name == name).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

        return self

    # def __repr__(self) -> str:
    #     return f"Palooza(id={self.id!r}, name={self.name!r}, description={self.description!r})"
