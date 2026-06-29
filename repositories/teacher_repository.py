from database.connection import get_connection
from psycopg2.extras import RealDictCursor

class TeacherRepository:

    def get_all_teachers(self):

        connection = get_connection()

        cursor = connection.cursor(
            cursor_factory=RealDictCursor
        )

        query = """
               SELECT
                   teacher_id,
                   teacher_name,
                   username,
                   email,
                   phone,
                   is_active
                FROM teachers
                ORDER BY teacher_name;
                
            """
        cursor.execute(query)

        teachers = cursor.fetchall()

        cursor.close()
        connection.close()

        return teachers
    
    def add_teacher(
        self,
        teacher_name,
        username,
        password,
        email,
        phone
    ):
        connection = get_connection()

        cursor = connection.cursor(
            cursor_factory = RealDictCursor
        )

        query = """
            INSERT INTO teachers
            (
                teacher_name,
                username,
                password,
                email,
                phone
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s
            )
            RETURNING teacher_id;
        """

        cursor.execute(
            query,
            (
                teacher_name,
                username,
                password,
                email,
                phone

            )
        )

        teacher = cursor.fetchone()

        connection.commit()

        cursor.close()
        connection.close()

        return teacher
    
    def update_teacher(
           self,
           teacher_id,
           teacher_name,
           username,
           password,
           email,
           phone

           ):
        
        connection = get_connection()

        cursor = connection.cursor(
            cursor_factory=RealDictCursor
        )

        query = """
            UPDATE teachers
            SET
                teacher_name = %s,
                username = %s,
                password = %s,
                email = %s,
                phone = %s
            WHERE teacher_id = %s
            RETURNING teacher_id;
         """
        print(
            teacher_id,
            teacher_name,
            username,
            password,
            email,
            phone
            )
        
        cursor.execute(
            query,
            (
                teacher_name,
                username,
                password,
                email,
                phone,
                teacher_id
                
            )
        )

        teacher = cursor.fetchone()

        connection.commit()

        cursor.close()
        connection.close()

        return teacher
    
    def delete_teacher(
            self,
            teacher_id
    ):
        
        connection = get_connection()

        cursor = connection.cursor(
            cursor_factory=RealDictCursor
        )

        query = """
            UPDATE teachers
            SET is_active = false
            WHERE teacher_id = %s
            RETURNING teacher_id;
        """

        cursor.execute(
            query,
            (teacher_id,)
        )

        teacher = cursor.fetchone()

        print("Repository:",teacher)

        connection.commit()

        cursor.close()
        connection.close()

        return teacher