"""
menu.py

This module defines the `Menu` class and pre-defined menu selections for the reversed Tic Tac Toe game.
It provides functionality for displaying various menus in a formatted layout, including the main menu,
bot difficulty selection, friend game options, round options, and save confirmation.

Classes:
    - Menu: Represents a menu with a title, selectable options, and a customizable column layout.

Pre-defined Menus:
    - main_menu_selection: The main menu options.
    - bot_menu_selection: Options for selecting bot difficulty.
    - friend_menu_selection: Options for playing with a friend.
    - round_menu_selection: Options for continuing or restarting a game round.
    - save_menu_selection: Options for confirming or canceling save actions.

Dependencies:
    - colorama: Used for colored terminal output.
"""

# Pre-defined menu selections
main_menu_selection = {
    1: "Play vs. Bot",
    2: "Play vs. Friend",
    3: "Player Profile",
    4: "How to Play",
    5: "Settings",
    6: "Quit"
}

bot_menu_selection = {
    1: "Easy",
    2: "Medium",
    3: "Difficult",
    4: "Back to Main Menu"
}

friend_menu_selection = {
    1: "Start Game",
    2: "Set Friend's Name",
    3: "Back to Main Menu"
}

round_menu_selection = {
    1: "Keep Playing",
    2: "New Game",
    3: "Back to Main Menu"
}

save_menu_selection = {
    1: "Cancel",
    2: "Proceed"
}

class Menu:
    """
    Represents a menu with a title, selectable options, and a customizable column layout.

    Attributes:
        title (str): The title of the menu.
        selection (dict): A dictionary mapping option numbers to their corresponding labels.
        columns (int): The number of columns to display the menu options in.
        width (int): The total width of the menu display.
    """

    def __init__(self, title:str, selection:dict, columns:int) -> None:
        """
        Initializes a new Menu instance.

        Args:
            title (str): The title of the menu.
            selection (dict): A dictionary mapping option numbers to their corresponding labels.
            columns (int): The number of columns to display the menu options in.
        """

        self.title = title
        self.selection = selection
        self.columns = columns
        self.width = 132

    def display(self) -> None:
        """
        Displays the menu in a formatted layout with the specified title, options, and column layout.
        Uses the `colorama` library for colored text.
        """

        from colorama import Fore, Style

        def break_line(border: str, char: str) -> str:
            return f'{border}{char * ((self.width - (len(border) * 2)) + 1)}{border}'

        # Heading
        print(f"\n{Style.BRIGHT}{break_line(border = "  ", char = "-")}")
        print(f"{Style.BRIGHT}|{Fore.BLUE}{self.title.upper():^{self.width - 1}}{Fore.RESET}|")

        print(f"{Style.BRIGHT}{break_line(border = "  ", char = "-")}")
        print(f"{Style.BRIGHT}{break_line(border = "|", char = " ")}")

        # Options
        total_options = len(self.selection)
        rows = (total_options + self.columns - 1) // self.columns
        col_width = (self.width - self.columns) // self.columns

        for row in range(rows):
            print(f"{Style.BRIGHT}|", end="")

            for col in range(1, self.columns + 1):
                option = col + (self.columns * row)

                if option in self.selection:
                    text = f'[{option:1}] {self.selection[option]}'
                    print(f"{Style.BRIGHT}{Fore.BLUE}{f'{text:^{col_width}}'}{Fore.RESET}|", end="")
                else:
                    print(f"{Style.BRIGHT}{" ":^{col_width}}|", end="")

            print(f"\n{Style.BRIGHT}{break_line(border = "|", char = " ")}")

        print(f"{Style.BRIGHT}{break_line(border = "  ", char = "-")}\n")
