from repositories.teacher_repository import TeacherRepository

class TeacherService:

    def __init__(self):
        self.teacher_repository = TeacherRepository()

    def get_all_teachers(self):
        return self.teacher_repository.get_all_teachers()
    
    def add_teacher(
            self,
            teacher_name,
            username,
            password,
            email,
            phone
    ):
        return self.teacher_repository.add_teacher(
            teacher_name,
            username,
            password,
            email,
            phone
        )
    
    def update_teacher(
            self,
            teacher_id,
            teacher_name,
            username,
            password,
            email,
            phone
    ):
        return self.teacher_repository.update_teacher(
            teacher_id,
            teacher_name,
            username,
            password,
            email,
            phone
        )
    
    def delete_teacher(
            self,
            teacher_id
    ):
        return self.teacher_repository.delete_teacher(
            teacher_id
        )
