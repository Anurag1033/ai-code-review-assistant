from sqlalchemy import (
    Column,
    Integer,
    Text,
    String,
    DateTime
)

from datetime import datetime

from app.db.database import Base


class Review(Base):

    __tablename__ = "reviews"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    code = Column(
        Text,
        nullable=False
    )

    language = Column(
        String,
        nullable=False
    )

    review = Column(
        Text,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )