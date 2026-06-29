from database.connection import get_connection
from psycopg2.extras import RealDictCursor

class StudentRepository:

    def get_all_students(self):

        connection = get_connection()

        cursor = connection.cursor(cursor_factory=RealDictCursor)

        query = """
            SELECT
                 s.student_id,
                 s.student_name,
                 s.gender,
                 TO_CHAR(s.date_of_birth, 'DD-MM-YYYY') AS date_of_birth,
                 c.class_name,
                 s.is_active
            FROM students s
            JOIN classes c
                ON s.class_id = c.class_id
            ORDER BY c.class_name, s.student_name;
        """

        cursor.execute(query)

        students = cursor.fetchall()

        cursor.close()
        connection.close()

        return students
    
    #POST 

    def add_student(self,student_name,gender,date_of_birth,class_id):
        
        connection = get_connection()

        cursor = connection.cursor(
            cursor_factory=RealDictCursor
        )

        query = """
            INSERT INTO students
            (
                student_name,
                gender,
                date_of_birth,
                class_id
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s
            )
            RETURNING student_id;
            
        """

        cursor.execute(
            query,
            (
                student_name,
                gender,
                date_of_birth,
                class_id
            )
        )

        student = cursor.fetchone()

        connection.commit()

        cursor.close()
        connection.close()

        return student
    
    def update_student(
            self,
            student_id,
            student_name,
            gender,
            date_of_birth,
            class_id
    ):
        connection = get_connection()

        cursor = connection.cursor(
            cursor_factory=RealDictCursor
        )

        query = """
            UPDATE students
            SET
                student_name = %s,
                gender = %s,
                date_of_birth = %s,
                class_id = %s
            WHERE student_id = %s
            RETURNING student_id;
        """

        cursor.execute(
            query,
            (
                student_name,
                gender,
                date_of_birth,
                class_id,
                student_id
            )
        )

        student = cursor.fetchone()

        connection.commit()

        cursor.close()
        connection.close()

        return student
    
    def delete_student(
            self,
            student_id
    ):
        connection = get_connection()

        cursor = connection.cursor(
            cursor_factory=RealDictCursor
        )

        query = """
            UPDATE students
            SET
                is_active = FALSE
            WHERE student_id = %s
            RETURNING student_id;
        """

        cursor.execute(
            query,
            (student_id,)
        )

        student = cursor.fetchone()

        connection.commit()

        cursor.close()
        connection.close()

        return student