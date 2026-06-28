from repositories.student_repository import StudentRepository

class StudentService:

    def __init__(self):
        self.student_repository = StudentRepository()

    def get_all_students(self):
        return self.student_repository.get_all_students()
    
    def add_student(self,student_name,gender,date_of_birth,class_id):

        return self.student_repository.add_student(student_name,gender,date_of_birth,class_id)
    
    def delete_student(
            self,
            student_id
    ):
        return self.student_repository.delete_student(
            student_id
        )