from services.student_service import StudentService

class StudentController:

    def __init__(self):
        self.student_service = StudentService()

    def get_all_students(self):
        return self.student_service.get_all_students()
    
    def add_student(self,student_name,gender,date_of_birth,class_id):
        return self.student_service.add_student(student_name,gender,date_of_birth,class_id)
    
    def delete_student(
            self,
            student_id
    ):
        return self.student_service.delete_student(
            student_id
        )
