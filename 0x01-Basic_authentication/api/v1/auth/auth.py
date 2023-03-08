#!/usr/bin/env python3
""" """
from flask import request
from typing import List, TypeVar


class Auth:
    """ """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ """
        if path is None:
            return True
        if not excluded_paths:
            return True
        if path in excluded_paths:
            return False
        else:
            for paths in excluded_paths:
                if paths.startswith(path):
                    return False
                if path.startswith(paths):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """ """
        if request is None:
            return None
        header = request.headers.get('Authorization')
        if header is None:
            return None
        else:
            return header

    def current_user(self, request=None) -> TypeVar('User'):
        return None
