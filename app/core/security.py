import base64
import hashlib
import hmac
import json
from datetime import datetime, timedelta, timezone


def hash_value(value: str, salt: str = "") -> str:
    raw = f"{salt}{value}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def verify_value(value: str, hashed_value: str, salt: str = "") -> bool:
    return hmac.compare_digest(hash_value(value, salt=salt), hashed_value)


def create_access_token(subject: str, expires_delta: timedelta | None = None) -> str:
    expires_at = datetime.now(timezone.utc) + (expires_delta or timedelta(hours=1))
    payload = {"sub": subject, "exp": expires_at.isoformat()}
    encoded = base64.urlsafe_b64encode(json.dumps(payload).encode("utf-8"))
    return encoded.decode("utf-8")
