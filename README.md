# Token Smith

This is a small toy project written in Python to explore and understand
authentication tokens, with a focus on **JWT** and **SAML**.

The goal of this repository is **learning**, not production readiness.

---

## What this project covers

- Creating and signing JWTs
- Validating and decoding JWTs
- Basic JWT authentication flow
- Generating and parsing SAML assertions
- Understanding the differences between JWT and SAML
- Common pitfalls and security considerations (at a high level)

---

## What this project is NOT

- A production-ready authentication system
- A full identity provider (IdP)
- A replacement for mature auth libraries or services

---

## Tech stack

- Python 3.x
- PyJWT (for JWT handling)
- python-saml / lxml (for SAML experiments)

---

## Why this exists

JWT and SAML are widely used but often treated as “magic”.
This project exists to demystify them by building and inspecting
the flows step by step.

---

## Getting started

```bash
git clone https://github.com/your-username/token-smith.git
cd token-smith
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
````

---

## Disclaimer

This project is for educational purposes only.
Do not use this code directly in production.

````

---

## Optional nice touch (highly recommended)

Add a tiny **learning roadmap** so reviewers know you’re intentional:

```md
## Learning roadmap

- [ ] JWT structure and signing
- [ ] JWT validation and expiration
- [ ] Refresh tokens
- [ ] SAML assertions and XML signatures
- [ ] Comparing JWT vs SAML use cases
