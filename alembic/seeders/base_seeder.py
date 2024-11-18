import psycopg2
from dotenv import load_dotenv
import os
from datetime import datetime


class BaseSeeder:
    def __init__(self):
        load_dotenv()

        self.connection_params = {
            'dbname': os.getenv('DB_NAME'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'host': os.getenv('DB_HOST'),
            'port': os.getenv('DB_PORT')
        }

    def connect(self):
        try:
            self.connection = psycopg2.connect(**self.connection_params)
            self.cursor = self.connection.cursor()
            print("Connected to the database for seeding.")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to database:", error)

    def close(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("PostgreSQL connection is closed.")

    def seed(self):
        raise NotImplementedError("Subclasses must implement the seed method")

    def run(self):
        try:
            self.connect()
            self.seed()
            self.connection.commit()
            print("Data has been seeded.")
        except (Exception, psycopg2.Error) as error:
            print("Error while seeding data:", error)
        finally:
            self.close()
