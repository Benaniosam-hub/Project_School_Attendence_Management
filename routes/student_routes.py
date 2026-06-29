from flask import Blueprint, request

from controllers.student_controller import StudentController

student_bp = Blueprint("student_bp",__name__)

student_controller = StudentController()

@student_bp.route("/students", methods = ["GET"])
def get_all_students():

    students = student_controller.get_all_students()

    return {
        "students": students
    }

@student_bp.route("/students",methods=["POST"])
def add_student():

    data = request.get_json()

    student = student_controller.add_student(
        data["student_name"],
        data["gender"],
        data["date_of_birth"],
        data["class_id"]
    )

    return {
        "message": "Student added successfully.",
        "student": student
    }, 201

@student_bp.route("/students/<student_id>", methods=["PUT"])
def update_student(student_id):

    data = request.get_json()

    student = student_controller.update_student(
        student_id,
        data["student_name"],
        data["gender"],
        data["date_of_birth"],
        data["class_id"]
    )

    return {
        "message": "Student updated successfully.",
        "student": student
    }

@student_bp.route("/students/<student_id>",methods=["DELETE"])
def delete_student(student_id):

    student = student_controller.delete_student(
        student_id
    )

    return {
        "message": "Student deleted successfully.",
        "student": student
    }
