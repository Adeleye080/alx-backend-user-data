#!/usr/bin/env python3
""" Basic Authentication Module """
import base64
from api.v1.auth.auth import Auth
from typing import TypeVar

from models.user import User


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

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ Extract user credentials from decoded header """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        credentials = decoded_base64_authorization_header.split(':')
        return (credentials[0], credentials[1])

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ """
        if not isinstance(user_email, str) or user_email is None:
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
            if not users or users == []:
                return None
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user

            return None
        except Exception:
            return None
