from fastapi import APIRouter, Header, HTTPException

from app.core.security import create_jwt, verify_jwt

router = APIRouter(prefix="/auth/jwt")


@router.post("/login")
def login(username: str):
    # fake auth
    token = create_jwt(
        subject=username,
        scope=["user"] if username != "admin" else ["admin"],
    )
    return {"access_token": token}


def jwt_auth(authorization: str = Header(...)):
    scheme, token = authorization.split()
    if scheme.lower() != "bearer":
        raise HTTPException(401, "Invalid auth scheme")
    return verify_jwt(token)
