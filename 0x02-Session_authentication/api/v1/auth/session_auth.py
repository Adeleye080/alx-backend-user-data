#!/usr/bin/env python3
"""
Module handles SimpleAPI session Authorization.
"""
from models.user import User

from .auth import Auth
from uuid import uuid4
from typing import TypeVar


class SessionAuth(Auth):
    """
    Session Authorization protocol.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create Session ID for user
        params:
            - user_id (str): user's ID
        Return:
            - None if user_id is None or not a string
            - Session ID (str)
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        id = str(uuid4())
        self.user_id_by_session_id[id] = user_id
        return id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Retrieves user ID by session ID
        params:
            - session_id (str): current session ID
        Return:
            - None if session_id is None or not a string
        """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves current user using session cookie
        """
        if self.session_cookie(request) is not None:
            usr_id = self.user_id_for_session_id(self.session_cookie(request))
            return User.get(usr_id)

    def destroy_session(self, request=None):
        if request is None:
            return False
        if self.session_cookie(request) is None:
            return False
        if not self.user_id_for_session_id(self.current_user(request)):
            del user_id_by_session_id[self.session_cookie(request)]
