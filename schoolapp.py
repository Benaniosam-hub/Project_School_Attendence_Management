from flask import Flask

from routes.class_routes import class_bp
from routes.teacher_routes import teacher_bp
from routes.student_routes import student_bp
from routes.attendance_routes import attendance_bp
from routes.login_routes import login_bp

app = Flask(__name__)

app.register_blueprint(class_bp)
app.register_blueprint(teacher_bp)
app.register_blueprint(student_bp)
app.register_blueprint(attendance_bp)
app.register_blueprint(login_bp)


@app.route("/")
def home():
    return {
        "message": "School Management API is running."
    }


if __name__ == "__main__":
    app.run(debug=True)