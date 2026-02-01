from dataclasses import dataclass


@dataclass
class User:
    """
    Protocol-agnostic representation of an authenticated user.
    """

    subject: str
    roles: list[str]
    attributes: dict
