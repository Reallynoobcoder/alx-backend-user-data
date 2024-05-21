#!/usr/bin/env python3
"""Class BasicAuth that inherits from Auth."""
from .auth import Auth
import base64


class BasicAuth(Auth):
    """Class BasicAuth that inherits from Auth."""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extracts the Base64 part of the Authorization
            header for Basic Authentication."""
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        base64_part = authorization_header[len('Basic '):]

        return base64_part

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Returns the decoded value of a Base64 string."""
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None

        try:
            decoded_base64 = base64.b64decode(
                base64_authorization_header, validate=True)
            return decoded_base64.decode('utf-8')
        except Exception:
            return None
