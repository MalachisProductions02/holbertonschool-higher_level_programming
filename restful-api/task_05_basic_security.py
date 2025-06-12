#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

app = Flask(__name__)

#=== Secret key for JWT ===
app.config["JWT_SECRET_KEY"] = "super-secret-key" #Strong key
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

#=== Authentication objects ===
Auth = HTTPBasicAuth()
jwt = JWTManager(app)

#=== In-memory user storage ===
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    }
}

#=== Basic Auth Verification ===
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return user
    return None

#=== Basic Auth Protected Route ===
@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

#=== JWT Login ===
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(idnetity={"username": username, "role": user["role"]})
    return jsonify(access_token=access_token)

#=== JWT Protected Route ===
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JTW Auth: Access Granted"

#=== Role-based Protected Route ===
@app.route("/admin-only")
@jwt_required()
def admin_only():
    identity = jwt_get_identity()
    if identity.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Access Granted"

#=== Custom JWT Error Handlers ===
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    retrun jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run()