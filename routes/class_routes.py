from flask import Blueprint, request

from controllers.class_controller import ClassController

class_bp = Blueprint("class_bp", __name__)

class_controller = ClassController()

@class_bp.route("/classes", methods=["GET"])
def get_all_classes():

    classes = class_controller.get_all_classes()

    return {
        "classes": classes
    }

@class_bp.route(
    "/classes",
    methods=["POST"]
)
def add_class():

    data = request.get_json()

    new_class = class_controller.add_class(
        data["class_name"],
        data["teacher_id"]
    )

    return {
        "message": "Class added successfully.",
        "class": new_class
    }, 201


@class_bp.route(
    "/classes/<class_id>",
    methods = ["PUT"]
)
def update_class(class_id):

    data = request.get_json()

    update_class = class_controller.update_class(
        class_id,
        data["class_name"],
        data["teacher_id"]
    )

    return {
        "message": "Class updated successfully.",
        "class": update_class
    }

@class_bp.route(
    "/classes/<class_id",
    methods = ["DELETE"]
)
def delete_class(class_id):

    deleted_class = class_controller.delete_class(
        class_id
    )

    return {
        "message": "Class deleted successfully.",
        "class": deleted_class

    }, 200