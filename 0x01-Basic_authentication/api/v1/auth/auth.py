#!/usr/bin/env python3
"""A class to manage the API authentication."""
from flask import Request
from typing import List, TypeVar


class Auth:
    """A class to manage the API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for a given path."""
        return True

    def authorization_header(self, request=None) -> str:
        """Extract authorization header from the Flask request object."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieve the current user based on the Flask request object."""
        return None
