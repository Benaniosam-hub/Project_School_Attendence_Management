from repositories.attendance_repository import AttendanceRepository


class AttendanceService:

    def __init__(self):
        self.attendance_repository = AttendanceRepository()

    def get_all_attendance(self):

        return self.attendance_repository.get_all_attendance()
    
    def add_attendance(
            self,
            student_id,
            teacher_id,
            attendance_date,
            session,
            status,
            remarks
    ):
        return self.attendance_repository.add_attendance(
            student_id,
            teacher_id,
            attendance_date,
            session,
            status,
            remarks
        )
    
    def update_attendance(
            self,
            attendance_id,
            student_id,
            teacher_id,
            attendance_date,
            session,
            status,
            remarks
    ):
        return self.attendance_repository.update_attendance(
            attendance_id,
            student_id,
            teacher_id,
            attendance_date,
            session,
            status,
            remarks
        )
    
    def delete_attendance(
            self,
            attendance_id
    ):
        return self.attendance_repository.delete_attendance(
            attendance_id
        )