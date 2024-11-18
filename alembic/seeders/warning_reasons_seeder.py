import psycopg2
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

connection_params = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT')
}

try:
    connection = psycopg2.connect(**connection_params)
    cursor = connection.cursor()
    print("Connected to the database for seeding.")

    reasons = [
        'Reason A',
        'Reason B',
        'Reason C'
    ]

    insert_query = '''
    INSERT INTO 
        warning_reasons (reason, created, updated)
    VALUES 
        (%s, %s, %s)
    '''


    for record in reasons:
        now = datetime.now()
        cursor.execute(insert_query, (
            record,
            now,
            now
        ))

    connection.commit()
    print("Data has been seeded.")

except (Exception, psycopg2.Error) as error:
    print("Error while seeding data:", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed.")
