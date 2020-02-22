import sqlite3
from datetime import datetime

from util import build_now_string, build_past_string

database_name = "test_data/sensors.db"

def execute_query(query):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    # Execute the query
    cursor.execute(query)

    return cursor.fetchone()

def get_average_value(column_name: str, time_offset: int):
    now = datetime.now()
    now_string = build_now_string(now)
    past_string = build_past_string(now, time_offset)
    query = f"SELECT avg({column_name}) FROM sensors WHERE date_time BETWEEN '{past_string}' AND '{now_string}'"

    return execute_query(query)[0]

def get_most_recent_value(column_name: str):

    query = f"SELECT date_time, {column_name} FROM sensors"

    return execute_query(query)