import hashlib
import hmac

from app.utils.config import settings


def verify_signature(payload: bytes, signature: str | None) -> bool:
    if signature is None:
        print("No GitHub signature received.")
        return False

    expected = (
        "sha256="
        + hmac.new(
            settings.GITHUB_WEBHOOK_SECRET.encode(),
            payload,
            hashlib.sha256,
        ).hexdigest()
    )

    print("Received :", signature)
    print("Expected :", expected)

    return hmac.compare_digest(expected, signature)