from services.teacher_service import TeacherService

class TeacherController:

    def __init__(self):
        self.teacher_service = TeacherService()

    def get_all_teachers(self):

        teachers = self.teacher_service.get_all_teachers()

        return teachers


    def add_teacher(
            self,
            teacher_name,
            username,
            password,
            email,
            phone
    ):
        return self.teacher_service.add_teacher(
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
        return self.teacher_service.update_teacher(
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
        return self.teacher_service.delete_teacher(
            teacher_id
        )
    
    def login_teacher(
            self,
            username,
            password
    ):
        return self.teacher_service.login_teacher(
            username,
            password
        )
    

