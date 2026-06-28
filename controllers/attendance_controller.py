from services.attendance_service import AttendanceService


class AttendanceController:

    def __init__(self):
        self.attendance_service = AttendanceService()

    def get_all_attendance(self):

        return self.attendance_service.get_all_attendance()
    
    def add_attendance(
            self,
            student_id,
            teacher_id,
            attendance_data,
            session,
            status,
            remarks
    ):
        return self.attendance_service.add_attendance(
            student_id,
            teacher_id,
            attendance_data,
            session,
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
        return self.attendance_service.update_attendance(
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
        return self.attendance_service.delete_attendance(
            attendance_id
        )


