USERS = {
    "alice": {"password": "password123", "roles": ["user"]},
    "bob": {"password": "password456", "roles": ["admin"]},
}


def authenticate(username: str, password: str) -> dict[str, str] | None:
    user = USERS.get(username)
    if user and user["password"] == password:
        return {"username": username, "roles": user["roles"]}
    return None
