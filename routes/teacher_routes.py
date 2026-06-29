from flask import Blueprint, request

from controllers.teacher_controller import TeacherController

teacher_bp = Blueprint("teacher_bp",__name__)

teacher_controller = TeacherController()

@teacher_bp.route("/teachers", methods= ["GET"])
def get_all_teachers():

    teachers = teacher_controller.get_all_teachers()

    return {
        "teachers": teachers
    }

@teacher_bp.route(
    "/teachers",
    methods=["POST"]
)
def add_teacher():

    data = request.get_json()

    teacher = teacher_controller.add_teacher(
        data["teacher_name"],
        data["username"],
        data["password"],
        data["email"],
        data["phone"]
    )

    return {
        "message": "Teacher added successfully.",
        "teacher": teacher
    }, 201

@teacher_bp.route(
    "/teachers/<teacher_id>",
    methods=["PUT"]
)
def update_teacher(teacher_id):

    data = request.get_json()

    teacher = teacher_controller.update_teacher(
        teacher_id,
        data["teacher_name"],
        data["username"],
        data["password"],
        data["email"],
        data["phone"]
    )

    return {
        "message": "Teacher updated successfully.",
        "teacher": teacher 
    }

@teacher_bp.route(
    "/teachers/<teacher_id>",
    methods =["DELETE"]
)

def delete_teacher(teacher_id):

    teacher = teacher_controller.delete_teacher(
        teacher_id
    )

    return {
        "message": "Teacher deleted successfully.",
        "teacher": teacher
    }, 200