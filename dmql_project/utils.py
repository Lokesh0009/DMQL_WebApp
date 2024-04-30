import psycopg2
from django.conf import settings

def get_table_names():
    """Fetches and returns all table names from the database."""
    # Establish a connection to the database
    conn = psycopg2.connect(
        dbname=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
        port=settings.DATABASES['default']['PORT']
    )
    cursor = conn.cursor()

    # Query to get table names
    cursor.execute("""
        SELECT table_name FROM information_schema.tables 
        WHERE table_schema='public'
    """)

    # Fetch all table names
    tables = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Extract and return table names as a list
    return [table[0] for table in tables]
