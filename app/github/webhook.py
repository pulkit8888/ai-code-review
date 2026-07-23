from fastapi import (
    APIRouter,
    Request,
    Header,
    Depends
)

from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.models.repository import Repository
from app.models.pull_request import PullRequest
from app.models.webhook_event import WebhookEvent


router = APIRouter()


@router.post("/webhook")
async def github_webhook(
    request: Request,
    x_github_event: str = Header(None),
    x_github_delivery: str = Header(None),
    db: Session = Depends(get_db)
):

    payload = await request.json()


    print("GitHub Event:", x_github_event)

    print(
        "Delivery ID:",
        x_github_delivery
    )


    # -----------------------------
    # Prevent duplicate deliveries
    # -----------------------------

    existing_event = db.query(
        WebhookEvent
    ).filter(
        WebhookEvent.delivery_id == x_github_delivery
    ).first()


    if existing_event:

        return {
            "status": "duplicate ignored"
        }



    webhook_event = WebhookEvent(
        delivery_id=x_github_delivery,
        event_type=x_github_event
    )


    db.add(webhook_event)

    db.commit()



    # -----------------------------
    # Process Pull Request event
    # -----------------------------

    if x_github_event == "pull_request":


        repo_data = payload["repository"]


        repo_name = repo_data["name"]

        owner_name = repo_data["owner"]["login"]



        # Check existing repository

        repository = db.query(
            Repository
        ).filter(
            Repository.name == repo_name,
            Repository.owner == owner_name
        ).first()



        if not repository:

            repository = Repository(
                name=repo_name,
                owner=owner_name
            )

            db.add(repository)

            try:
                db.commit()
                db.refresh(repository)

            except Exception:
                db.rollback()

                repository = db.query(
                    Repository
                ).filter(
                    Repository.name == repo_name,
                    Repository.owner == owner_name
                ).first()



        pr_data = payload["pull_request"]



        pull_request = PullRequest(
            repository_id=repository.id,
            pr_number=pr_data["number"],
            branch=pr_data["head"]["ref"],
            commit_sha=pr_data["head"]["sha"],
            author=pr_data["user"]["login"],
            action=payload["action"],
            status="received"
        )


        db.add(pull_request)

        db.commit()



    return {
        "status": "stored",
        "event": x_github_event
    }