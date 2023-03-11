#!/usr/bin/env python3
"""
Module handles SimpleAPI session Authorization.
"""
from .auth import Auth
from uuid import uuid4


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
