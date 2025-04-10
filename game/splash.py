import keyboard, os
from colorama import init, Fore, Style
from time import sleep

init(autoreset=True)

def load(text: str) -> None:
    os.system("cls")

    # Terminal
    term_size = os.get_terminal_size()
    term_width = term_size.columns
    term_height = term_size.lines

    # Loading Bar
    bar_width = 100
    animation_char = '█'
    padding_top = (term_height // 2) - 2

    # Static Elements
    title_line = f"{text:^{term_width}}"
    border_line = f"{' ' * ((term_width - bar_width - 4) // 2)}  {'-' * bar_width}  "

    # Center Vertically
    print("\n" * padding_top, end="")

    # Display Loading Animation
    print(Style.BRIGHT + title_line)
    print(border_line)

    for bar in range(bar_width + 1):
        filled = animation_char * bar
        empty = ' ' * (bar_width - bar)
        progress_bar = f"| {filled}{empty} |"
        progress_line = f"{' ' * ((term_width - len(progress_bar)) // 2)}{Fore.GREEN + progress_bar + Style.RESET_ALL}"
        print(progress_line)

        print(border_line)

        print(f"\033[F\033[F", end='', flush=True) # Move cursor up 2 lines

        sleep(0.02)

    print(f"\033[E", end='')  # Move cursor down 1 line

    sleep(1)

    os.system("cls")

def full(text:str) -> None:
    os.system("cls")

    size = os.get_terminal_size()

    print("\n" * (size.lines // 2))

    for index in range(1, len(text) + 1):
        print(Style.BRIGHT + Fore.LIGHTGREEN_EX + f'{" " * ((size.columns - len(text)) // 2)}' + text[:index], end="\r", flush=True)
        sleep(0.1)

    keyboard.wait('enter')

    os.system("cls")

def title() -> None:
    init(autoreset=True)

    print(Style.BRIGHT + r'''

 ----------     ----------     ----------     ----------     ----------     ----------     ----------     ----------     ----------
|          |   |          |   |          |   |          |   |          |   |          |   |          |   |          |   |    ---   |
 ---    ---     ---    ---    |   -------     ---    ---    |    --    |   |   -------     ---    ---    |    --    |   |   |___|  |
    |  |           |  |       |  |               |  |       |   |  |   |   |  |               |  |       |   |  |   |   |   -------
    |  |           |  |       |  |               |  |       |    --    |   |  |               |  |       |   |  |   |   |  |
    |  |        ---    ---    |   -------        |  |       |    --    |   |   -------        |  |       |    --    |   |   -------
    |  |       |          |   |          |       |  |       |   |  |   |   |          |       |  |       |          |   |          |
     --         ----------     ----------         --         ---    ---     ----------         --         ----------     ----------

 ----------     ----------     ---    ---     ----------     ----------     ----------     ----------     ---------      ----------
|    --    |   |    ---   |   |   |  |   |   |    ---   |   |    --    |   |          |   |    ---   |   |         -    |  -    -  |
|   |  |   |   |   |___|  |   |   |  |   |   |   |___|  |   |   |  |   |   |   |------    |   |___|  |   |   ----   |   | |.|  |.| |
|    --    |   |   -------    |   |  |   |   |   -------    |    --    |   |   |______    |   -------    |  |    |  |   |  -    -  |
|    --   -    |  |           |   |  |   |   |  |           |    --   -    |          |   |  |           |  |    |  |   |  ------  |
|   |  \  \    |   -------     \   \/   /    |   -------    |   |  \  \     -----|    |   |   -------    |   ----   |   | |||||||| |
|   |   \  \   |          |     \      /     |          |   |   |   \  \   |          |   |          |   |         -    |  ------  |
 ---     ---    ----------       ------       ----------     ---     ---    ----------     ----------     ---------      ----------
    ''')
