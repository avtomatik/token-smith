import base64

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import RedirectResponse

from app.core.clock import now
from app.core.saml_xml import build_authn_request, parse_assertion
from app.core.trust import is_trusted_idp

router = APIRouter(prefix="/sp")


@router.get("/saml/login")
def saml_login():
    authn_request = build_authn_request(
        issuer="token-smith-sp",
        acs_url="http://localhost:8000/sp/saml/acs",
        issue_instant=now(),
    )

    encoded_request = base64.b64encode(authn_request.encode()).decode()

    return RedirectResponse(
        f"http://localhost:8000/idp/saml/login?SAMLRequest={encoded_request}"
    )


@router.post("/saml/acs")
def saml_acs(SAMLResponse: str):
    decoded_response = base64.b64decode(SAMLResponse).decode()
    assertion_data = parse_assertion(decoded_response)

    if not is_trusted_idp(assertion_data["issuer"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Untrusted IdP"
        )

    return {"user": assertion_data["subject"]}
