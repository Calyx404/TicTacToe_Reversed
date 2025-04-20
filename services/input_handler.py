"""
input_handler.py

This module provides utility functions for validating user input and displaying error alerts in the reversed Tic Tac Toe game.
It ensures that user inputs conform to specific requirements based on the context (e.g., menu selection, game moves, settings updates).

Functions:
    - validate(input_, type, **kwargs): Validates user input based on the specified type and additional constraints.
    - alert(error): Displays an error message in a formatted and colored style.

Dependencies:
    - colorama: Used for colored terminal output.
"""

from colorama import init, Fore, Style

def validate(input_:str, type:str, **kwargs) -> None:
    """
    Validates user input based on the specified type and additional constraints.

    Args:
        input_ (str): The user input to validate.
        type (str): The type of validation to perform. Supported types include:
            - "int": Validates numeric input.
                - "menu": Ensures the input corresponds to a valid menu option.
                - "settings": Ensures the input is within a valid range for settings.
                - "move": Ensures the input is a valid move on the game board.
            - "str": Validates alphabetic input.
                - "limit": Ensures the input does not exceed a character limit (e.g., 10 characters).
            - "mix": Validates alphanumeric input (must contain both letters and numbers).
                - "limit": Ensures the input does not exceed a character limit (e.g., 8 characters).
        **kwargs: Additional constraints for validation. Supported keys include:
            - selection (list): A list of valid options for menu or settings validation.
            - occupied (list): A list of already occupied cells for move validation.

    Raises:
        ValueError: If the input does not meet the specified validation criteria.
    """

    selection = kwargs.get('selection')
    occupied = kwargs.get('occupied', [])

    # Check if input is empty
    if not input_:
        raise ValueError("Missing input")

    # Check if input is numeric
    if "int" in type:
        if not input_.isdigit():
            raise ValueError("Not numeric")

        num = int(input_)

        if "menu" in type:
            if not selection or num < 1 or num > len(selection):
                raise ValueError("Not in option")

        if "settings" in type:
            if not selection or num < min(selection) or num > max(selection):
                raise ValueError("Not in option")

        if "move" in type:
            if not selection or num < 1 or num > (len(selection) ** 2):
                raise ValueError("Move not it range")
            if num in occupied:
                raise ValueError("Cell already occupied")

    # Check if input is alphabetic
    if "str" in type:
        if not input_.isalpha():
            raise ValueError("Only letters are allowed")

        if "limit" in type:
            if len(input_) > 10:
                raise ValueError("Maximum of 10 characters only")

    # Check if input is alphanumeric
    if "mix" in type:
        if not (any(char.isalpha() for char in input_) and any(char.isdigit() for char in input_)):
            raise ValueError("Must consist of letter and numbers")

        if "limit" in type:
            if len(input_) > 8:
                raise ValueError("Maximum of 8 characters only")

def alert(error) -> None:
    """
    Displays an error message in a formatted and colored style.

    Args:
        error (str): The error message to display.
    """

    init(autoreset=True)

    print(Fore.LIGHTRED_EX + Style.BRIGHT + f"Error : {error}\n")
