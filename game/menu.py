main_menu = {
    1: "Play vs. Bot",
    2: "Play vs. Friend",
    3: "Achievements",
    4: "How to Play",
    5: "Settings",
    6: "Quit"
}

bot_menu = {
    1: "Easy",
    2: "Medium",
    3: "Difficult",
    4: "Back to Main Menu"
}

friend_menu = {
    1: "Start Game",
    2: "Set Friend's Name",
    3: "Back to Main Menu"
}

round_menu = {
    1: "Keep Playing",
    2: "New Game",
    3: "Back to Main Menu"
}

save_menu = {
    1: "Cancel",
    2: "Save"
}

class Menu:
    def __init__(self, title:str, selection:dict, columns:int) -> None:
        self.title = title
        self.selection = selection
        self.columns = columns
        self.width = 132

    def display(self) -> None:

        from colorama import Fore, Style

        def break_line(border: str, char: str) -> str:
            return f'{border}{char * ((self.width - (len(border) * 2)) + 1)}{border}'

        # Heading
        print(f"\n{Style.BRIGHT}{break_line(border = "  ", char = "-")}")
        print(f"{Style.BRIGHT}|{Fore.BLUE}{f"{self.title.upper():^{self.width - 1}}"}{Fore.RESET}|")

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
