#!/usr/bin/env python3
""" Module for API authentication management """
from flask import request
from typing import List, TypeVar


class Auth():
    """Class to manage API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method to check if a path requires authentication"""

        if path is None:
            return True

        if not excluded_paths:
            return True

        normalized_path = path if path.endswith('/') else path + '/'

        for ex_path in excluded_paths:
            normalized_ex_path = ex_path if ex_path.endswith(
                '/') else ex_path + '/'
            if normalized_path == normalized_ex_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Method to get the authorization header from the request"""
        if request is None:
            return None

        if 'Authorization' not in request.headers:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Method to get the current user from the request"""
        return None
