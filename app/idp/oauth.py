from uuid import uuid4

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(prefix="/idp/oauth")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/idp/oauth/token")


@router.get("/authorize")
def oauth_authorize(
    client_id: str, redirect_uri: str, response_type: str = "code"
) -> RedirectResponse:
    if client_id != "my-client-id":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid client ID"
        )

    code = str(uuid4())
    return RedirectResponse(f"{redirect_uri}?code={code}")


@router.post("/token")
def oauth_token(
    grant_type: str, code: str, redirect_uri: str, client_id: str
) -> dict[str, str]:
    if grant_type != "authorization_code":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid grant type",
        )
    if client_id != "my-client-id":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid client ID"
        )

    return {"access_token": "fake-access-token", "token_type": "bearer"}
