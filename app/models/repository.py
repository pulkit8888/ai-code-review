from sqlalchemy import (
    Column,
    Integer,
    String,
    UniqueConstraint
)

from app.db.database import Base


class Repository(Base):

    __tablename__ = "repositories"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    name = Column(
        String,
        nullable=False
    )


    owner = Column(
        String,
        nullable=False
    )


    __table_args__ = (
        UniqueConstraint(
            "name",
            "owner",
            name="unique_repository"
        ),
    )