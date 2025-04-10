from colorama import init, Fore, Style, Back

main_menu = {
    1: "Play vs. Bot",
    2: "Play vs. Friend",
    3: "Achievements",
    4: "Mechanics",
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

        init(autoreset=True)

        break_line = lambda border, char : f'{border}{char * ((self.width - (len(border) * 2)) + 1)}{border}'

        print(Style.BRIGHT + "\n" + break_line(border = "  ", char = "-"))
        print(Style.BRIGHT + '|' + Fore.BLUE + f'{self.title.upper():^{self.width - 1}}' + Style.RESET_ALL + Style.BRIGHT + '|')
        print(Style.BRIGHT + break_line(border = "  ", char = "-"))

        print(Style.BRIGHT + break_line(border = "|", char = " "))

        for row in range((len(self.selection) + self.columns - 1) // self.columns):
            print(Style.BRIGHT + "|", end="")

            for col in range(1, self.columns + 1):
                option = col + (self.columns * row)

                if option in self.selection:
                    print(Style.BRIGHT + Fore.BLUE + f'{f'[{option:1}] {self.selection[option]}':^{(self.width - (self.columns)) // self.columns}}' + Style.RESET_ALL + Style.BRIGHT + '|', end="")
                else:
                    print(Style.BRIGHT + f'{" ":^{(self.width - (self.columns)) // self.columns}}|', end="")

            print(Style.BRIGHT + '\n' + break_line(border = "|", char = " "))

        print(Style.BRIGHT + break_line(border = "  ", char = "-") + "\n")
