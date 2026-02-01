# OAuth 2.0 / OpenID Connect Flow

## Purpose
Delegated authentication via third-party IdP.

## Flow (Authorization Code)
1. User redirected to IdP
2. User authenticates
3. IdP redirects back with code
4. SP exchanges code for tokens
5. SP validates ID token
6. SP issues its own JWT

## Key distinctions
- OAuth ≠ authentication
- OIDC adds identity layer

## Failure modes
- Code reuse
- Redirect URI mismatch
- Invalid audience
