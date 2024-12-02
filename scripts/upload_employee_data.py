import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Read database connection details from environment variables
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

# Define the path to your CSV file
csv_file_path = 'scripts/mock_employee_data.csv'

def upload_data_to_mysql(csv_file_path):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Connect to the MySQL database
    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        cursor = connection.cursor()

        # Loop through each row in the DataFrame and insert into the database
        for index, row in df.iterrows():
            cursor.execute("""
                INSERT INTO employees (
                    employee_id, first_name, last_name, date_of_birth, address, 
                    email, phone, hire_date, job_title, status, 
                    department_id, role_id, manager_id
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, tuple(row))

        # Commit the transaction
        connection.commit()
        print(f"Successfully uploaded {len(df)} records to the database.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

# Upload the data
upload_data_to_mysql(csv_file_path)