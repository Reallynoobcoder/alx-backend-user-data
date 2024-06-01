#!/usr/bin/env python3
"""Flask app."""
from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def main():
    """A basic Flask app that returns a jsonify message."""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users():
    """End-point to register a user."""
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """Log in end point."""
    email = request.form.get("email")
    password = request.form.get("password")

    if Auth.valid_login(email, password):
        session_id = Auth.create_session(email)
        response = make_response(
            jsonify({"email": email, "message": "logged in"}))
        response.set_cookie("session_id", session_id)
        return response

    else:
        return abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
