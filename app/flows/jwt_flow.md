# JWT Flow

## Purpose
Stateless authorization for API requests.

## Token issuance
- Issuer: auth-playground
- Audience: auth-playground-api
- Lifetime: short-lived


## Request flow
1. Client sends Authorization: Bearer <JWT>
2. API verifies signature
3. API validates claims (exp, iss, aud)
4. API enforces authorization via scopes

## Security properties
- Integrity via signature
- No built-in revocation
- Audience-scoped

## Failure modes
- Expired token
- Wrong audience
- Tampered payload
