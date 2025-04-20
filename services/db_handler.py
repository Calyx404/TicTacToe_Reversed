"""
db_handler.py

This module provides utility functions for handling database operations related to player accounts
in the reversed Tic Tac Toe game. It includes functionality for checking the existence of the database file,
loading data from the database, and saving data back to the database.

Functions:
    - _check_file(): Ensures the database file exists; creates it if it does not.
    - _load_data(): Loads and returns the data from the database file.
    - _save_data(data): Saves the provided data to the database file.

Dependencies:
    - os: Used to check the existence of the database file.
    - json: Used to read and write data in JSON format.

Constants:
    - ACCOUNTS_DB (str): The file path to the accounts database.
"""

import os, json

ACCOUNTS_DB = "./runtime/data/accounts.json"

def _check_file() -> None:
    """
    Ensures the database file exists. If the file does not exist, it creates an empty JSON file.

    This function is typically called during the initialization of the application to ensure
    that the database file is ready for use.

    Raises:
        OSError: If there is an issue creating the file.
    """

    if not os.path.exists(ACCOUNTS_DB):
        with open(ACCOUNTS_DB, "w") as file:
            json.dump({}, file)

def _load_data() -> dict:
    """
    Loads and returns the data from the database file.

    Returns:
        dict: The data stored in the database file. If the file is empty, an empty dictionary is returned.

    Raises:
        JSONDecodeError: If the file contains invalid JSON.
        FileNotFoundError: If the database file does not exist.
    """

    with open(ACCOUNTS_DB, "r") as file:
        return json.load(file)

def _save_data(data:dict) -> None:
    """
    Saves the provided data to the database file.

    Args:
        data (dict): The data to save to the database file.

    Raises:
        TypeError: If the provided data is not serializable to JSON.
        OSError: If there is an issue writing to the file.
    """

    with open(ACCOUNTS_DB, "w") as file:
        json.dump(data, file, indent=4)
