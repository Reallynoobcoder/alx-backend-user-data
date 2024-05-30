#!/usr/bin/env python3
"""Auth."""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Hash a password into bytes."""

    pwd = password.encode('utf-8')

    salt = bcrypt.gensalt()

    hash_password = bcrypt.hashpw(pwd, salt)

    return hash_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user."""
        if self._db.find_user_by(email=email):
            raise ValueError("User {} already exists".format(email))

        hashed_password = _hash_password(password)

        user = self._db.add_user(email=email, hashed_password=hashed_password)

        return user
