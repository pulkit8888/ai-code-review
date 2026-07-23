from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from app.db.database import Base


class PullRequest(Base):

    __tablename__ = "pull_requests"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    repository_id = Column(
        Integer,
        ForeignKey(
            "repositories.id"
        )
    )


    pr_number = Column(
        Integer,
        nullable=False
    )


    branch = Column(
        String
    )


    commit_sha = Column(
        String
    )


    author = Column(
        String
    )

    action = Column(
        String
    )

    status = Column(
        String,
        default="received"
    )