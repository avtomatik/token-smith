import base64
from datetime import datetime, timezone

from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="/idp")


SP_ACS_URL = "http://localhost:800/sp/saml/acs"
IDP_ENTITY_ID = "fake-idp"


@router.get("/saml/login")
def login_form(SAMLRequest: str) -> HTMLResponse:
    return HTMLResponse(
        """
        <h2>Fake Indentity Provider</h2>
        <p>Authenticate as:</p>
        <form method="post">
            <input name="user" value="alice"/>
            <button type="submit">Login</button>
        </form>
    """
    )


@router.post("/saml/login")
def login_post(user: str = Form(...)) -> HTMLResponse:
    assertion = f"""
    <Assertion>
        <Issuer>{IDP_ENTITY_ID}</Issuer>
        <Subject>{user}</Subject>
        <IssuedAt>{datetime.now(tz=timezone.utc).isoformat()}</IssuedAt>
    </Assertion>
    """

    encoded_assertion = base64.b64encode(assertion.encode()).decode()

    return HTMLResponse(
        f"""
        <h3>Authentication successful</h3>
        <form action="{SP_ACS_URL}" method="post">
            <input type="hidden" name="SAMLResponse" value="{encoded_assertion}" />
            <button type="submit">Continue to Service Provider</button>
        </form>
    """
    )
