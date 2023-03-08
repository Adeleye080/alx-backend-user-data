#!/usr/bin/env python3
""" Basic Authentication Module """
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ Manage Basic Authentication """
    def extract_base64_authorization_header(self, authorization_header: str)\
            -> str:
        """ Extracts Authentication details for Basic Authentication
        Return:
            - client encoded Basic Auth details
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(' ')[-1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """ Decodes base64 auth """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            auth_str = base64_authorization_header.encode('utf-8')
            auth_str = base64.b64decode(auth_str)
            return auth_str.decode('utf-8')
        except Exception:
            return None
