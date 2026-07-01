import bcrypt
from repositories.teacher_repository import TeacherRepository
from utils.auth import verify_password, create_token

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
        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()    
        ).decode("utf-8")

        return self.teacher_repository.add_teacher(
            teacher_name,
            username,
            hashed_password,
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
    
    def login_teacher(
            self,
            username,
            password
    ):
        teacher = self.teacher_repository.login_teacher(
            username
        )

        if teacher is None:
            return None
        if not teacher["is_active"]:
            return None
        if not verify_password(
            password,
            teacher["password"]
        ):
            return None
        
        token = create_token(
            teacher["teacher_id"]
        )

        return {
            "teacher_id": teacher["teacher_id"],
            "username": teacher["username"],
            "token": token
        }
