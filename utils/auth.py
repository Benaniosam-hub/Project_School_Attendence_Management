import jwt
import bcrypt
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