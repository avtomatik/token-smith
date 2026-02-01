from dataclasses import dataclass
from datetime import datetime


@dataclass
class Token:
    """
    Logical representation of an access token.
    """

    subject: str
    issuer: str
    audience: str
    issued_at: datetime
    expires_at: datetime
    scopes: list[str]
