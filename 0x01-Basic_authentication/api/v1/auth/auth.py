#!/usr/bin/env python3
"""A class to manage the API authentication."""
from flask import Request
from typing import List, TypeVar


class Auth:

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for a given path."""
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request: Request = None) -> str:
        """Extract authorization header from the Flask request object."""
        if request is None:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieve the current user based on the Flask request object."""
        return None
