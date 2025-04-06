main_menu = {
    1: "Play vs. Bot",
    2: "Play vs. Friend",
    3: "Profile",
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

round_menu = {
    1: "Resume Game",
    2: "New Game",
    3: "Save and Exit",
    4: "Back to Main Menu"
}

class Menu:
    def __init__(self, title:str, selection:dict, columns:int, width:int = 132):
        self.title = title
        self.selection = selection
        self.columns = columns
        self.width = width

    def display(self):

        break_line = lambda border, char : f'{border}{char * (self.width - 1)}{border}'

        print(break_line(border = " ", char = "-"))
        print(f'|{self.title.upper():^{self.width - 1}}|')
        print(break_line(border = " ", char = "-"))

        print(break_line(border = "|", char = " "))

        for row in range((len(self.selection) + self.columns - 1) // self.columns):
            print("|", end="")

            for col in range(1, self.columns + 1):
                option = col + (self.columns * row)

                if option in self.selection:
                    print(f'{f'[{option:1}] {self.selection[option]}':^{(self.width - (self.columns)) // self.columns}}|', end="")
                else:
                    print(f'{" ":^{(self.width - (self.columns)) // self.columns}}|', end="")

            print(f'\n|{" " * (self.width - 1)}|')

        print(break_line(border = " ", char = "-"), "\n")
