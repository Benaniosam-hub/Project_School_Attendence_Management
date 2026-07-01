import jwt
import bcrypt

from functools import wraps
from flask import request, jsonify, g
from datetime import datetime, timedelta, UTC

SECURITY_KEY = "school_management_secret"

def hash_password(password):
    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

def verify_password(password, hashed_password):
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )

def create_token(teacher_id):
    payload = {
        "teacher_id": teacher_id,
        "exp": datetime.now(UTC) + timedelta(hours=2)
    }

    token = jwt.encode(
        payload,
        SECURITY_KEY,
        algorithm="HS256"
    )

    return token 

def verify_token(token):
    try:
        payload = jwt.decode(
            token,
            SECURITY_KEY,
            algorithms = ["HS256"]
        )
        return payload
    
    except jwt.ExpiredSignatureError:
        return None
    
    except jwt.InvalidTokenError:
        return None
    
def jwt_required(function):
    @wraps(function)
    def decorated(*args, **kwargs):

        auth_header = request.headers.get("Authorization")

        if auth_header is None:
            return jsonify({
                "message": "Token is missing."
            }), 401
        
        if not auth_header.startswith("Bearer "):
            return jsonify({
                "message": "Invalid token format."
            }), 401
        
        token = auth_header.split(" ")[1]

        payload = verify_token(token)

        if payload is None:
            return jsonify({
                "message": "Invalid or expired token."
            }), 401
        
        g.teacher_id = payload["teacher_id"]

        return function(*args, **kwargs)
    
    return decorated