import sqlite3
import time
from datetime import datetime

from util import build_now_string, build_past_string

test_database_name = "test_data/sensors.db"
database_name = "../automation_framework_python/framework/database/databases/sensors.db"


def execute_query(query):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    result = None
    for try_count in range(0, 3):

        # Execute the query
        try:
            cursor.execute(query)
            result = cursor.fetchone()
            break

        except sqlite3.OperationalError:

            time.sleep(.25)

    cursor.close()
    connection.close()

    return result

def get_average_value(column_name: str, time_offset: int):

    now = datetime.now()
    now_string = build_now_string(now)
    past_string = build_past_string(now, time_offset)
    query = f"SELECT avg({column_name}) FROM sensors WHERE date_time BETWEEN '{past_string}' AND '{now_string}'"

    result = execute_query(query)
    return result[0] if result is not None else None

def get_most_recent_value(column_name: str):

    query = f"SELECT date_time, {column_name} FROM sensors ORDER BY date_time DESC"

    return execute_query(query)

def get_output_state(output_name: str):

    query = f"SELECT date_time, output_state FROM output_states WHERE output_name = '{output_name}'"
    return execute_query(query)
