import sqlalchemy as sa
from sqlalchemy import orm
from datetime import datetime

from features.product.schemas.schema import Base


class ProductSchema(Base):
    """Product Model"""

    __tablename__ = "products"

    id: orm.Mapped[int] = orm.mapped_column(
        primary_key=True,
        autoincrement=True,
    )
    name: orm.Mapped[str] = orm.mapped_column(
        sa.String(32),
        nullable=False,
    )
    price: orm.Mapped[int] = orm.mapped_column(nullable=False)

    created_at: orm.Mapped[datetime] = orm.mapped_column(default=datetime.now)
    updated_at: orm.Mapped[datetime] = orm.mapped_column(
        default=datetime.now,
        onupdate=datetime.now,
    )

    def __repr__(self) -> str:
        return f"ProductSchema(id={self.id!r}, name={self.name!r})"
