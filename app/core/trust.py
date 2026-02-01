from app.core.keys import JWT_AUDIENCE, JWT_ISSUER

TRUSTED_IDPS = ["fake-idp"]


def is_trusted_idp(issuer: str) -> bool:
    return issuer in TRUSTED_IDPS


def is_valid_audience(audience: str) -> bool:
    return audience == JWT_AUDIENCE


def is_valid_issuer(issuer: str) -> bool:
    return issuer == JWT_ISSUER
