from app.db.database import Base, engine

from app.models.repository import Repository
from app.models.pull_request import PullRequest
from app.models.webhook_event import WebhookEvent

print("Creating ReviewFlow database tables...")


Base.metadata.create_all(
    bind=engine
)


print("Tables created successfully")