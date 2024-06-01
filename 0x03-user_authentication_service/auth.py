#!/usr/bin/env python3
"""Auth."""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """Hash a password into bytes."""

    pwd = password.encode('utf-8')

    salt = bcrypt.gensalt()

    hash_password = bcrypt.hashpw(pwd, salt)

    return hash_password


def _generate_uuid() -> str:
    """Generate a string representation of a new UUID."""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user."""
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            pass
        hashed_password = _hash_password(password)

        user = self._db.add_user(email=email, hashed_password=hashed_password)

        return user

    def valid_login(self, email: str, password: str) -> bool:
        """Valide login."""
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
            else:
                return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Create session ID as a string."""
        user = self._db.find_user_by(email=email)

        try:
            new_uuid = _generate_uuid()

            user.session_id = new_uuid

            self._db.update_user(user.id, session_id=new_uuid)

            return new_uuid
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id):
        """Find user by session ID and return None if no user is found."""
        if session_id is None:
            return None

        try:
            session = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return session

    def destroy_session(self, user_id: int) -> None:
        """Destroy a session based on user_id."""
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """Generates and returns a reset password token for a user."""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        
        new_token = _generate_uuid()
        self._db.update_user(user.id, reset_token=new_token)
        return new_token
