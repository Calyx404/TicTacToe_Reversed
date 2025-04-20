"""
splash.py

This module provides utility functions for displaying visual elements and animations in the terminal.
It includes functions for clearing the screen, displaying banners, animating text, and rendering ASCII art.
These utilities are used to enhance the user experience in the reversed Tic Tac Toe game.

Functions:
    - clear(): Clears the terminal screen.
    - wait(key, name, action, end): Waits for a specific key press to continue.
    - typing(text, speed): Animates text as if it is being typed.
    - load(text): Displays a loading animation with a progress bar.
    - line(fore, pattern): Displays a horizontal line with a repeating pattern.
    - label(text): Displays a labeled section header.
    - hint(text): Displays a hint or informational message.
    - ascii(text, fore): Renders ASCII art for a given text in a specified color.
    - start(): Displays the game's introductory animation and prompts.
    - banner(): Displays the game's banner with ASCII art and patterns.

Dependencies:
    - colorama: Used for colored terminal output.
    - time.sleep: Used for delays in animations.
    - os: Used for clearing the terminal screen.
    - msvcrt: Used for detecting key presses on Windows systems.
"""

from colorama import init, Fore, Style
from time import sleep

init(autoreset=True)

# Global
term_width = 134
term_middle = lambda : print("\n" * 17)

def clear() -> None:
    """
    Clears the terminal screen.
    """

    from os import system, name
    system('cls' if name == 'nt' else 'clear')

def wait(key:bytes, name:str, action:str, end:str = None) -> None:
    """
    Waits for a specific key press to continue.

    Args:
        key (bytes): The key to wait for (e.g., b' ' for space).
        name (str): The name of the key (e.g., "space").
        action (str): The action to display (e.g., "continue").
        end (str, optional): An optional end character for the message.
    """

    from msvcrt import kbhit, getch

    if end is None:
        print(f"{Style.DIM}{f"PRESS '{name.upper()}' TO {action.upper()}":^{term_width}}")

    else:
        print(f"{Style.DIM}{f"PRESS '{name.upper()}' TO {action.upper()}":^{term_width}}", end="\r", flush=True)

    while True:
        if kbhit():
            if getch() == key:
                break

def typing(text:str, speed:float) -> None:
    """
    Animates text as if it is being typed.

    Args:
        text (str): The text to animate.
        speed (float): The delay between each character in seconds.
    """

    for index in range(1, len(text) + 1):
        print(f"{Style.BRIGHT}{text[:index]:^{term_width}}", end="\r", flush=True)
        sleep(speed)

    print("\n")

def load(text: str) -> None:
    """
    Displays a loading animation with a progress bar.

    Args:
        text (str): The text to display above the progress bar.
    """

    clear()

    bar_width = 100
    animation_char = '█'
    bar_padding = ' ' * ((term_width - bar_width) // 2)

    term_middle()
    print(Style.BRIGHT + f"{text:^{term_width}}\n")

    for bar in range(bar_width + 1):
        filled = animation_char * bar
        empty = ' ' * (bar_width - bar)
        progress_bar = f"{Fore.GREEN}{filled}{empty}"

        print(f"{bar_padding}{progress_bar}", end="\r", flush=True)
        sleep(0.01)

    sleep(1)
    clear()

def line(fore:str, pattern:str) -> None:
    """
    Displays a horizontal line with a repeating pattern.

    Args:
        fore (str): The color of the line (e.g., "GREEN", "RED").
        pattern (str): The pattern to repeat across the line.
    """

    if fore.upper() == "GREEN":
        print(Fore.GREEN + f"\n{pattern * (term_width // len(pattern)):^{term_width}}\n")
    if fore.upper() == "RED":
        print(Fore.RED + f"\n{pattern * (term_width // len(pattern)):^{term_width}}\n")
    if fore.upper() == "YELLOW":
        print(Fore.YELLOW + f"\n{pattern * (term_width // len(pattern)):^{term_width}}\n")
    if fore.upper() == "WHITE":
        print(Fore.WHITE + f"\n{pattern * (term_width // len(pattern)):^{term_width}}\n")

def label(text:str) -> None:
    """
    Displays a labeled section header.

    Args:
        text (str): The text to display as the label.
    """

    print(f"\n{Style.BRIGHT}-> {Fore.BLUE}{text.upper()}{Fore.RESET} {"-" * (term_width - (len(text) + 5))}{Style.RESET_ALL}\n")

def hint(text:str) -> None:
    """
    Displays a hint or informational message.

    Args:
        text (str): The hint text to display.
    """

    print(f"{Style.BRIGHT}{Fore.BLUE}[?] {text}{Style.RESET_ALL}")

def ascii(text:str, fore:str) -> None:
    """
    Renders ASCII art for a given text in a specified color.

    Args:
        text (str): The text to render as ASCII art.
        fore (str): The color of the ASCII art (e.g., "BLUE", "CYAN").
    """

    letters = {
        "A": [
            " ---------- ",
            "|██████████|",
            "|███|‾‾|███|",
            "|███|__|███|",
            "|██████████|",
            "|███ -- ███|",
            "|███|  |███|",
            " ---    --- ",
        ],
        "B": [
            " ---        ",
            "|███|       ",
            "|███ ------ ",
            "|██████████|",
            "|███|‾‾|███|",
            "|███|__|███|",
            "|██████████|",
            " ---------- ",
        ],
        "C": [
            " ---------- ",
            "|██████████|",
            "|███ ------ ",
            "|███|       ",
            "|███|       ",
            "|███ ------ ",
            "|██████████|",
            " ---------- ",
        ],
        "D": [
            " ---------  ",
            "|█████████| ",
            "|███|‾‾|███|",
            "|███|  |███|",
            "|███|  |███|",
            "|███|__|███|",
            "|█████████| ",
            " --------   ",
        ],
        "E": [
            " ---------- ",
            "|██████████|",
            "|███|‾‾|███|",
            "|██████████|",
            "|███ ------ ",
            "|███|       ",
            "|██████████|",
            " ---------- ",
        ],
        "F": [
            " ---------- ",
            "|██████████|",
            "|███ ------ ",
            "|███|       ",
            "|██████████|",
            "|███ ------ ",
            "|███|       ",
            " ---        ",
        ],
        "G": [
            " ---------- ",
            "|██████████|",
            "|███ ------ ",
            "|███|       ",
            "|██████████|",
            "|███|‾‾|███|",
            "|██████████|",
            " ---------- ",
        ],
        "H": [
            " ---        ",
            "|███|       ",
            "|███ ------ ",
            "|██████████|",
            "|███|  |███|",
            "|███|  |███|",
            "|███|  |███|",
            " ---    --- ",
        ],
        "I": [
            " ---------- ",
            "|██████████|",
            " --- ██ --- ",
            "    |██|    ",
            "    |██|    ",
            " --- ██ --- ",
            "|██████████|",
            " ---------- ",
        ],
        "J": [
            "        --- ",
            "       |███|",
            "       |███|",
            " ---   |███|",
            "|███|  |███|",
            "|███|  |███|",
            "|██████████|",
            " ---------- ",
        ],
        "K": [
            " ---    --- ",
            "|███|  |███|",
            "|███||███| ",
            "|█████|    ",
            "|█████|    ",
            "|███||███| ",
            "|███|  |███|",
            " ---    --- ",
        ],
        "L": [
            " ---        ",
            "|███|       ",
            "|███|       ",
            "|███|       ",
            "|███|       ",
            "|███ ------ ",
            "|██████████|",
            " ---------- ",
        ],
        "M": [
            " ---------- ",
            "|██████████|",
            "|██--██--██|",
            "|██||██||██|",
            "|██||██||██|",
            "|██| -- |██|",
            "|██|    |██|",
            " --      -- ",
        ],
        "N": [
            " ---------- ",
            "|██████████|",
            "|███ -- ███|",
            "|███|  |███|",
            "|███|  |███|",
            "|███|  |███|",
            "|███|  |███|",
            " --      -- ",
        ],
        "O": [
            " ---------- ",
            "|██████████|",
            "|███|‾‾|███|",
            "|███|  |███|",
            "|███|  |███|",
            "|███|__|███|",
            "|██████████|",
            " ---------- ",
        ],
        "P": [
            " ---------- ",
            "|██████████|",
            "|███|‾‾|███|",
            "|███|__|███|",
            "|██████████|",
            "|███ ------ ",
            "|███|       ",
            " ---        ",
        ],
        "Q": [
            " ---------- ",
            "|██████████|",
            "|███|‾‾|███|",
            "|███|__|███|",
            "|██████████|",
            " ------ ███|",
            "       |███|",
            "        --- ",
        ],
        "R": [
            " ---------- ",
            "|██████████|",
            "|███|‾‾|███|",
            "|███|  |███|",
            "|███|   --- ",
            "|███|       ",
            "|███|       ",
            " ---        ",
        ],
        "S": [
            " ---------- ",
            "|██████████|",
            "|███|------ ",
            "|███|______ ",
            "|██████████|",
            " ------|███|",
            "|██████████|",
            " ---------- ",
        ],
        "T": [
            " ---------- ",
            "|██████████|",
            " --- ██ --- ",
            "    |██|    ",
            "    |██|    ",
            "    |██|    ",
            "    |██|    ",
            "     --     ",
        ],
        "U": [
            " ---    --- ",
            "|███|  |███|",
            "|███|  |███|",
            "|███|  |███|",
            "|███|  |███|",
            "|███ -- ███|",
            "|██████████|",
            " ---------- ",
        ],
        "V": [
            " ---    --- ",
            "|███|  |███|",
            "|███|  |███|",
            "|███|  |███|",
            "|███|  |███|",
            " |███--███| ",
            "  |██████|  ",
            "   ------   ",
        ],
        "W": [
            " --      -- ",
            "|██|    |██|",
            "|██| -- |██|",
            "|██||██||██|",
            "|██||██||██|",
            "|██--██--██|",
            "|██████████|",
            " ---------- ",
        ],
        "X": [
            " ---    --- ",
            "|███|  |███|",
            " |███||███| ",
            "    |██|    ",
            "    |██|    ",
            " |███||███| ",
            "|███|  |███|",
            " ---    --- ",
        ],
        "Y": [
            " --      -- ",
            "|███|  |███|",
            "|███ -- ███|",
            "|██████████|",
            " --- ██ --- ",
            "    |██|    ",
            "    |██|    ",
            "     --     ",
        ],
        "Z": [
            " ---------- ",
            "|██████████|",
            " ----- ███| ",
            "    |███|   ",
            "  |███|     ",
            " |███ ----- ",
            "|██████████|",
            " ---------- ",
        ],
        "🤖": [
            " ---------- ",
            "|██████████|",
            "|█|.|██|.|█|",
            "|██████████|",
            "|██████████|",
            "|█||||||||█|",
            "|██████████|",
            " ---------- ",
        ],
    }

    text = text.upper()

    for row in range(8):
        line = ""
        for index, char in enumerate(text):
            if char in letters:
                if index == (len(text) - 1):
                    line += letters[char][row]

                else:
                    line += letters[char][row] + "   "

            else:
                line += " " * 12 + "   "

        if fore.upper() == "BLUE":
            print(Style.BRIGHT + Fore.BLUE + f"{line:^{term_width}}")

        if fore.upper() == "CYAN":
            print(Style.BRIGHT + Fore.CYAN + f"{line:^{term_width}}")

        if fore.upper() == "GREEN":
            print(Style.BRIGHT + Fore.GREEN + f"{line:^{term_width}}")

        if fore.upper() == "RED":
            print(Style.BRIGHT + Fore.RED + f"{line:^{term_width}}")

        if fore.upper() == "YELLOW":
            print(Style.BRIGHT + Fore.YELLOW + f"{line:^{term_width}}")

def start() -> None:
    """
    Displays the game's introductory animation and prompts.

    The animation includes a series of frames with text that introduces the game's concept and rules.
    """

    frames = [
        "They told you to win. They lied.",
        "Every move whispers from the void, luring you closer to your own demise.",

        "Tic-Tac-Toe? Oh, you think you know it?",
        "But what if the goal was to lose… and you didn't see it coming?",

        "This is the twisted grid — form a line, and you fall.",
        "Resist. Deceive. And whatever you do…",
        "DON'T WIN.",

        "Welcome to Tic-Tac-Toe: Reversed!",
    ]

    for frame in frames:
        clear()
        term_middle()
        typing(text=frame, speed=0.045)
        print()
        wait(key=b' ', name="space", action="continue")

    clear()
    term_middle()
    typing(text="Tell me... how long can you outplay yourself?", speed=0.045)
    print()
    wait(key=b'\r', name="enter", action="start game")

    clear()
    load(text="Loading Game")

def banner() -> None:
    """
    Displays the game's banner with ASCII art and patterns.
    """

    line(fore="white", pattern="-X-O")

    ascii(text="TICTACTOE", fore="CYAN")
    ascii(text="REVERSED🤖", fore="CYAN")

    line(fore="white", pattern="O-X-")
