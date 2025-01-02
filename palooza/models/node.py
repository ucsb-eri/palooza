
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_serializer import SerializerMixin

from palooza import db


class Node(db.Model, SerializerMixin):
    __tablename__ = "nodes"
    serialize_rules = ("-palooza_id", "-palooza")

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    palooza_id: Mapped[int] = mapped_column(ForeignKey("paloozas.id"))
    palooza: Mapped["Palooza"] = relationship(back_populates="nodes")

    @classmethod
    def find_by_name(cls, name):
        return Node.query.filter(Node.name == name).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

        return self

    def __repr__(self) -> str:
        return f"Node(id={self.id!r}, name={self.name!r})"
