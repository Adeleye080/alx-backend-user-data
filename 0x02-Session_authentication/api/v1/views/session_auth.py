#!/usr/bin/env python3
"""
Handles all route for session authentication
"""
from api.v1.views import app_views
from flask import jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session():
    """
    Compares user inputed email and password with the one in database
    Return:
        - Error: if user email or password doesn't match with stored user info.
        - User object (json): if inputed email and password matched.
    """
    # checks if user login details are supplied
    if request.form.get('email') is None:
        return jsonify({'error': 'email missing'}), 400
    if request.form.get('password') is None:
        return jsonify({'error': 'password missing'}), 400
    # stores user inputed details in variable
    email = request.form.get('email')
    password = request.form.get('password')
    # search database for user using sipplied credentials
    users = User.search({'email': email})
    if users is None or users == []:
        return jsonify({'error': 'no user found for this email'}), 404
    for user in users:
        if not user.is_valid_password(password):
            return jsonify({'error': 'wrong password'}), 401
        from api.v1.auth.session_auth import SessionAuth
        ses = SessionAuth()
        ses_ID = ses.create_session(user.id)
        resp = jsonify(user.to_json())
        # sets user session cookie
        resp.set_cookie(getenv('SESSION_NAME'), ses_ID)
    return resp
