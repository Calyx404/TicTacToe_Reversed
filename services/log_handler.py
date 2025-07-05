"""
log_handler.py

This module provides a utility function for logging application activities and events.
It writes log entries to a specified log file, including timestamps, log levels, and activity descriptions.

Functions:
    - log(level, activity): Logs an activity with a specified log level and timestamp.

Dependencies:
    - datetime: Used to generate timestamps for log entries.

Constants:
    - LOG_FILE (str): The file path to the application's log file.
"""

from datetime import datetime
from .db_handler import resource_path

LOG_FILE = resource_path("runtime/logs/app.log")

def log(level:str, activity:str) -> None:
    """
    Logs an activity with a specified log level and timestamp.

    Args:
        level (str): The severity level of the log (e.g., "INFO", "WARNING", "ERROR").
        activity (str): A description of the activity or event to log.

    Behavior:
        - Appends a log entry to the log file specified by `LOG_FILE`.
        - Each log entry includes the current timestamp, the log level, and the activity description.

    Log Format:
        [YYYY-MM-DD HH:MM:SS] [LEVEL] : Activity description

    Raises:
        OSError: If there is an issue writing to the log file.
    """

    with open(LOG_FILE, mode = "a") as logbook:
        log = logbook.write(f'[{datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')}] [{level.upper()}] : {activity}\n')
