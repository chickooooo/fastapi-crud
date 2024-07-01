import sqlalchemy as sa
from sqlalchemy import orm


# create database engine
ENGINE = sa.create_engine(
    "sqlite:///mydb.db",
    connect_args={"check_same_thread": False},
    echo=True,
)


class Base(orm.DeclarativeBase):
    """Declarative Base"""

    pass
