from sqlalchemy import Column, Integer, String

from app.db.database import Base


class WebhookEvent(Base):

    __tablename__ = "webhook_events"


    id = Column(
        Integer,
        primary_key=True
    )


    delivery_id = Column(
        String,
        unique=True,
        nullable=False
    )


    event_type = Column(
        String
    )