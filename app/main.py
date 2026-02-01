from fastapi import FastAPI

from app.idp import saml as idp_saml
from app.sp import jwt, oauth, protected
from app.sp import saml as sp_saml

app = FastAPI()

app.include_router(jwt.router)
app.include_router(sp_saml.router)
app.include_router(oauth.router)
app.include_router(protected.router)

app.include_router(idp_saml.router)
