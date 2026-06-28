import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="school_management",
        user="postgres",
        password="0000",
        port="5432"
    )