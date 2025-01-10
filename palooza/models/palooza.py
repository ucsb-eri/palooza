from typing import List, Optional

from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy_serializer import SerializerMixin

from palooza import db

palooza_node = Table(
    "palooza_node",
    db.Model.metadata,
    Column("palooza_id", ForeignKey("paloozas.id"), primary_key=True),
    Column("node_id", ForeignKey("nodes.id"), primary_key=True),
)


class Palooza(db.Model, SerializerMixin):
    __tablename__ = "paloozas"
    # serialize_only=("id")
    serialize_rules = ("-nodes.paloozas",)

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[Optional[str]]
    nodes: Mapped[List["Node"]] = relationship(
        secondary=palooza_node, back_populates="paloozas"
    )

    @classmethod
    def find_by_name(cls, name):
        return Palooza.query.filter(Palooza.name == name).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

        return self
