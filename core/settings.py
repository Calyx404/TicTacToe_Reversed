"""
settings.py

This module manages the settings and preferences for the reversed Tic Tac Toe game.
It provides functionality for account management, game preferences, and system controls.
The settings include options for signing in, signing up, updating profiles, resetting progress,
adjusting game preferences (e.g., grid size, time limit, first move), and deleting accounts.

Functions:
    - build_menu(): Builds the settings menu based on the player's login status.
    - sign_in(username, password): Signs the player into their account.
    - sign_up(username, password): Creates a new player account and signs in.
    - sign_out(): Signs the player out of their account.
    - reset_progress(): Resets the player's game progress.
    - reset_preferences(): Resets the player's game preferences to default values.
    - save_preferences(preference, value): Saves a specific game preference.
    - delete_account(): Deletes the player's account from the database.
    - update_profile(profile, value): Updates the player's username or password.
    - display(): Displays the settings menu in a formatted layout.

Dependencies:
    - player.Player: Manages player-related functionality such as account management and preferences.
    - colorama: Used for colored terminal output.
"""

from .player import Player

player = Player()

def build_menu():
    """
    Builds the settings menu based on the player's login status.

    Returns:
        dict: A dictionary mapping menu option numbers to their corresponding labels.
    """

    if player.logged_in:
        # Logged-in
        return {
            1: "Change Username",
            2: "Change Password",
            3: "Sign out",
            4: "Grid Size",
            5: "Time Limit",
            6: "First Move",
            7: "Reset Progress",
            8: "Reset Preferences",
            9: "Delete Account",
            10: "Save and Exit"
        }

    else:
        # Guest
        return {
            1: "Sign In",
            2: "Sign Up",
            3: "Grid Size",
            4: "Time Limit",
            5: "First Move",
            6: "Reset Preferences",
            7: "Save and Exit"
        }

menu = build_menu()

def sign_in(username:str, password:str) -> bool:
    """
    Signs the player into their account and updates the menu.

    Args:
        username (str): The player's username.
        password (str): The player's password.

    Returns:
        bool: True if the sign-in was successful.
    """

    player.sign_in(username=username, password=password)
    menu = build_menu()
    return True

def sign_up(username:str, password:str) -> bool:
    """
    Creates a new player account and signs in.

    Args:
        username (str): The desired username.
        password (str): The desired password.

    Returns:
        bool: True if the sign-up and sign-in were successful.
    """

    player.sign_up(username=username, password=password)
    return sign_in(username=username, password=password)

def sign_out() -> bool:
    """
    Signs the player out of their account and updates the menu.

    Returns:
        bool: True if the sign-out was successful.
    """

    player.sign_out()
    menu = build_menu()
    return True

def reset_progress() -> bool:
    """
    Resets the player's game progress.

    Returns:
        bool: True if the progress reset was successful.
    """

    player.reset_progress()
    return True

def reset_preferences() -> bool:
    """
    Resets the player's game preferences to default values.

    Returns:
        bool: True if the preferences reset was successful.
    """

    player.reset_preferences()
    return True

def save_preferences(preference:str, value:int) -> bool:
    """
    Saves a specific game preference.

    Args:
        preference (str): The name of the preference to update (e.g., "GRID_SIZE").
        value (int): The new value for the preference.

    Returns:
        bool: True if the preference was successfully saved.
    """

    if preference.upper() == "GRID_SIZE":
        player.save_preferences(grid_size=value)
    if preference.upper() == "TIME_LIMIT":
        player.save_preferences(time_limit=value)
    if preference.upper() == "FIRST_MOVE":
        player.save_preferences(first_move=value)

    return True

def delete_account() -> bool:
    """
    Deletes the player's account from the database and signs out.

    Returns:
        bool: True if the account deletion was successful.
    """

    player.delete_account(username=player.username)
    sign_out()
    return True

def update_profile(profile:str, value:str) -> bool:
    """
    Updates the player's profile information (username or password).

    Args:
        profile (str): The profile field to update ("USERNAME" or "PASSWORD").
        value (str): The new value for the profile field.

    Returns:
        bool: True if the profile update was successful.
    """

    if profile.upper() == 'USERNAME':
        player.update_profile(old_username=player.username, new_username=value)
    if profile.upper() == 'PASSWORD':
        player.update_profile(old_username=player.username, new_password=value)

    return True

def display() -> None:
    """
    Displays the settings menu in a formatted layout, including account, game preferences,
    and system control options. The menu dynamically adjusts based on the player's login status.
    """

    from colorama import Fore, Style

    term_width = 132
    col_width = (term_width - 3) // 3

    def break_line(border: str, char: str) -> str:
        """
        Creates a horizontal line for the menu display.

        Args:
            border (str): The border character (e.g., "|").
            char (str): The character to fill the line with.

        Returns:
            str: The formatted line string.
        """

        return f'{border}{char * ((term_width - (len(border) * 2)) + 1)}{border}'

    account_keys = ["Sign In", "Sign Up", "Change Username", "Change Password", "Sign Out"]
    system_keys = ["Reset Progress", "Delete Account", "Reset Preferences", "Save and Exit"]

    account, game, system = {}, {}, {}
    menu = build_menu()

    for key, label in menu.items():
        if any(label.lower().startswith(option.lower()) for option in account_keys):
            account[key] = label

        elif any(label.lower().startswith(option.lower()) for option in system_keys):
            system[key] = label

        else:
            game[key] = label

    columns = {
        "ACCOUNT & SECURITY": account,
        "GAME BEHAVIOR & PREFERENCES": game,
        "SYSTEM CONTROLS": system
    }

    max_rows = max(len(column) for column in columns.values())

    # Header
    print(f"\n{Style.BRIGHT}{break_line(border = "  ", char = "-")}")
    print(f"{Style.BRIGHT}|{Fore.BLUE}{'SETTINGS':^{term_width - 1}}{Fore.RESET}|")

    print(f"{Style.BRIGHT}{break_line(border = "  ", char = "-")}")
    print(f"{Style.BRIGHT}{break_line(border = "|", char = " ")}")

    print(f"{Style.BRIGHT}|", end="")
    for header in columns:
        print(f" {Style.BRIGHT}{Fore.BLUE}{header:{col_width - 1}}{Fore.RESET}|", end="")
    print()

    print(f"{Style.BRIGHT}{break_line(border = "|", char = " ")}")

    # Menu Items
    for row in range(max_rows):

        print(f"{Style.BRIGHT}|", end="")
        for col in columns:
            items = list(columns[col].items())

            if row < len(items):
                key, label = items[row]
                text = f" [{key}] {label}"

                if label == "Grid Size":
                    info = f"  ---> {player.grid_size}x{player.grid_size} "
                    print(f"{Style.BRIGHT}{Fore.BLUE}{text}{info:{col_width - len(text)}}{Fore.RESET}|", end="")
                elif label == "Time Limit":
                    info = f" ---> {player.time_limit}s "
                    print(f"{Style.BRIGHT}{Fore.BLUE}{text}{info:{col_width - len(text)}}{Fore.RESET}|", end="")
                elif label == "First Move":
                    info = f" ---> {"You " if player.first_move == 0 else "Opponent "}"
                    print(f"{Style.BRIGHT}{Fore.BLUE}{text}{info:{col_width - len(text)}}{Fore.RESET}|", end="")
                else:
                    print(f"{Style.BRIGHT}{Fore.BLUE}{text:{col_width}}{Fore.RESET}|", end="")

            else:
                print(f"{' ':{col_width}}|", end="")

        print(f"\n{Style.BRIGHT}{break_line(border = "|", char = " ")}")

    print(f"{Style.BRIGHT}{break_line(border = "  ", char = "-")}\n")
