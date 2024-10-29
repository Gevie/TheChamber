import psycopg2
from dotenv import load_dotenv
import os
import json
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

    # Read JSON data from file
    json_file_path = os.path.join(os.path.dirname(__file__), '../data/temperature_facts.json')
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        temperature_facts = json.load(json_file)

    insert_query = '''
    INSERT INTO temperature_facts (min_temperature, max_temperature, fact, created, updated)
    VALUES (%s, %s, %s, %s, %s);
    '''

    for record in temperature_facts:
        min_temp = record['min_temp']
        max_temp = record['max_temp']
        now = datetime.now()
        for fact in record['facts']:
            cursor.execute(insert_query, (
                min_temp,
                max_temp,
                fact,
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
