from database.connection import get_connection
from psycopg2.extras import RealDictCursor


class ClassRepository:

    def get_all_classes(self):

        connection = get_connection()

        cursor = connection.cursor(cursor_factory=RealDictCursor)

        query = """
            SELECT
                class_id,
                class_name,
                teacher_id
            FROM classes
            ORDER BY class_name;
        """

        cursor.execute(query)

        classes = cursor.fetchall()

        cursor.close()
        connection.close()

        return classes
    
    def add_class(self,class_name,teacher_id):
        
        connection = get_connection()

        cursor = connection.cursor(
            cursor_factory=RealDictCursor
        )

        query = """
            INSERT INTO classes
            (
                class_name,
                teacher_id
            )
            VALUES
            (
                %s,
                %s
                
            )
            RETURNING class_id;
        """

        cursor.execute(
            query,
            (
                class_name,
                teacher_id
            )
        )

        new_class = cursor.fetchone()

        connection.commit()

        cursor.close()
        connection.close()

        return new_class
        
    
    def update_class(
            self,
            class_id,
            class_name,
            teacher_id
    ):
        
        connection = get_connection()

        cursor =connection.cursor(
            cursor_factory=RealDictCursor
        )

        query = """
            UPDATE classes
            SET
                class_name = %s,
                teacher_id = %s,
            WHERE class_id = %s,
            RETURNING class_id;
        """

        cursor.execute(
            query,
            (
                class_name,
                teacher_id,
                class_id
            )
        )
        
        updated_class = cursor.fetchone()

        connection.commit()

        cursor.close()
        connection.close()

        return updated_class 
    
    def delete_class(
            self,
            class_id
    ):
        connection = get_connection()

        cursor = connection.cursor(
            cursor_factory=RealDictCursor
        )
        query = """
            DELETE FROM classes
            WHERE class_id = %s
            RETURNING class_id;
        """

        cursor.execute(
            query,
            (class_id,)
        )

        deleted_class = cursor.fetchone()

        connection.commit()

        cursor.close()
        connection.close()

        return deleted_class 

