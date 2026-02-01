from fastapi import Depends

from app.sp.jwt import jwt_auth, router


@router.get("/protected")
def protected(payload=Depends(jwt_auth)):
    return {
        "user": payload["sub"],
        "scope": payload["scope"],
    }
