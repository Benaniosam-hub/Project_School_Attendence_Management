from flask import Blueprint, request
from controllers.teacher_controller import TeacherController

login_bp = Blueprint("login_bp",__name__)
teacher_controller = TeacherController()

@login_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    teacher = teacher_controller.login_teacher(
        data["username"],
        data["password"]
    )

    if teacher is None:
        return {
            "message": "Invalid username or password."
        }, 401
    
    return {
        "message": "Login successful.",
        "teacher": teacher
    }, 200