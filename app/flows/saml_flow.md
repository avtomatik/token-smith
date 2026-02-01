# SAML Authentication Flow

## Roles
- Service Provider (SP): our application
- Identity Provider (IdP): fake-idp

## Flow

1. User accesses `/sp/saml/login`
2. SP creates AuthnRequest and redirects browser to IdP
3. IdP authenticates user
4. IdP issues signed assertion
5. Browser POSTs assertion to SP ACS endpoint
6. SP validates assertion and extracts subject
7. SP creates session or JWT

## Trust decisions
- SP trusts assertions only from `fake-idp`
- Assertion must be recent
- Assertion must not be replayed

## Failure modes
- Untrusted issuer
- Expired assertion
- Replay attack
