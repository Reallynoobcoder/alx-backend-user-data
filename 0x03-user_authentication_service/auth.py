#!/usr/bin/env python3
"""Auth."""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash a password into bytes."""

    pwd = password.encode('utf-8')

    salt = bcrypt.gensalt()

    hash_password = bcrypt.hashpw(pwd, salt)

    return hash_password
