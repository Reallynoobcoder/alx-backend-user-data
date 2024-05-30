#!/usr/bin/env python3
"""Flask app."""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def main():
    """a basic Flask app that returns a jsonify message."""
    return jsonify({"message": "Bienvenue"})
