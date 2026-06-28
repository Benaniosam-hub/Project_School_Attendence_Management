from database.connection import get_connection
from psycopg2.extras import RealDictCursor

class AttendanceRepository:

    def get_all_attendance(self):

        connection = get_connection()

        cursor = connection.cursor(
            cursor_factory=RealDictCursor
        )

        query = """
            SELECT
                a.attendance_id,
                s.student_name,
                c.class_name,
                t.teacher_name,
                TO_CHAR(a.attendance_date, 'DD-MM-YYYY') AS attendance_date,
                a.session,
                a.status,
                a.remarks
            FROM attendance a
            JOIN students s
                ON a.student_id = s.student_id
            JOIN classes c
                ON s.class_id = c.class_id
            JOIN teachers t
                ON a.teacher_id = t.teacher_id
            ORDER BY
                a.attendance_date DESC,
                c.class_name,
                s.student_name;
            """
        cursor.execute(query)

        attendance = cursor.fetchall()

        cursor.close()
        connection.close()

        return attendance
    
    def add_attendance(
            self,
            student_id,
            teacher_id,
            attendance_data,
            session,
            status,
            remarks
    ):
        connection = get_connection()

        cursor = connection.cursor(
            cursor_factory=RealDictCursor
        )

        query = """
            INSERT INTO attendance
            (
                student_id,
                teacher_id,
                attendance_data,
                session,
                status,
                remarks
            )
            
            VALUES
            
            (
            
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            )
            RETURNING attendance_id;
        """

        cursor.execute(
            query,
            (
                student_id,
                teacher_id,
                attendance_data,
                session,
                status,
                remarks
            )
        )

        attendance = cursor.fetchone()

        connection.commit()

        cursor.close()
        connection.close()

        return attendance
    
    def update_attendance(
            self,
            attendance_id,
            student_id,
            teacher_id,
            attendance_data,
            session,
            status,
            remarks
    ):
        connection = get_connection()

        cursor = connection.cursor(
            cursor_factory=RealDictCursor
        )

        query = """
            UPDATE attendance
            SET
                student_id = %s,
                teacher_id = %s,
                attendance_data = %s,
                session = %s,
                status = %s,
                remarks = %s
            WHERE attendance_id = %s
            RETURNING attendance_id;
        """

        cursor.execute(
            query,
            (
                student_id,
                teacher_id,
                attendance_data,
                session,
                status,
                remarks,
                attendance_id
            )
        )

        attendance = cursor.fetchone()

        connection.commit()

        cursor.close()
        connection.close()

        return attendance
    
    def delete_attendance(
            self,
            attendance_id
    ):
        
        connection = get_connection()

        cursor = connection.cursor(
            cursor_factory=RealDictCursor
        )

        query = """
            DELETE FROM attendance
            WHERE attendance_id = %s
            RETURNING attendance_id;
        """

        cursor.execute(
            query,
            (attendance_id,)
        )

        attendance = cursor.fetchone()

        connection.commit()

        cursor.close()
        connection.close()

        return attendance