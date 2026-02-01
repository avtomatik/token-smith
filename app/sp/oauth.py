from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(prefix="/sp/oauth")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/login")
def oauth_login(client_id: str, redirect_uri: str) -> JSONResponse:
    auth_url = f"http://localhost:8000/idp/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}"
    return JSONResponse({"redirect_to": auth_url})


@router.get("/callback")
def oauth_callback(
    code: str, client_id: str, redirect_uri: str
) -> JSONResponse:
    if client_id != "my-client-id":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid client ID"
        )

    access_token = "fake-access-token"

    return JSONResponse({"access_token": access_token, "token_type": "bearer"})
