from flask import Blueprint, request

from controllers.attendance_controller import AttendanceController


attendance_bp = Blueprint(
    "attendance_bp",
    __name__
)

attendance_controller = AttendanceController()


@attendance_bp.route(
    "/attendance",
    methods=["GET"]
)
def get_all_attendance():

    attendance = attendance_controller.get_all_attendance()

    return {
        "attendance": attendance
    }

@attendance_bp.route(
    "/attendance",
    methods=["POST"]
)
def add_attendance():

    data = request.get_json()

    attendance = attendance_controller.add_attendance(
        data["student_id"],
        data["teacher_id"],
        data["attendance_data"],
        data["session"],
        data["status"],
        data.get("remarks")
    )

    return {
        "message": "Attendance marked successfully.",
        "attendance": attendance
    }, 201


@attendance_bp.route(
    "/attendance/<attendance_id>",
    methods=["PUT"]
)
def update_attendance(attendance_id):

    data = request.get_json()

    attendance = attendance_controller.update_attendance(
        attendance_id,
        data["student_id"],
        data["teacher_id"],
        data["attendance_date"],
        data["session"],
        data["status"],
        data.get("remarks")
    )

    return {
        "message": "Attendance updated successfully.",
        "attendance": attendance
    }


@attendance_bp.route(
    "/attendance/<attendance_id",
    methods= ["DELETE"]
)

def delete_attendance(attendance_id):

    attendance = attendance_controller.delete_attendance(
        attendance_id
    )

    return {
        "message": "Attendance deleted successfully.",
        "attendance": attendance
    }, 200
