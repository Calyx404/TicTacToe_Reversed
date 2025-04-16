from random import choice
from time import sleep
from threading import Thread, Event

# Global
text = "Computer is thinking..."

def think(event:Event) -> None:

    from colorama import Fore, Style

    while not event.is_set():
        for index in range(1, len(text) + 1):
            if event.is_set():
                break

            print(" " * 50, end="\r", flush=True)
            print(f"{Style.BRIGHT}{Fore.RED}{f"Opponent's turn [O] : {text[:index]}"}", end="\r", flush=True)
            sleep(0.1)

    print(" " * 50, end="\r", flush=True)

def easy(size:int, delay:int, occupied:list[int] = []) -> int:

    thinking = Event()

    thinking.clear()
    thread = Thread(target=think, args=(thinking,))
    thread.start()

    sleep(delay)

    all_cells = list(range(1, size**2 + 1))
    available = [cell for cell in all_cells if cell not in occupied]
    move = choice(available) if available else None

    thinking.set()
    thread.join()

    return move

def medium(size:int, delay:int, occupied:list[int] = []) -> int:

    thinking = Event()

    thinking.clear()
    thread = Thread(target=think, args=(thinking,))
    thread.start()

    sleep(delay)

    all_cells = list(range(1, size**2 + 1))
    available = [cell for cell in all_cells if cell not in occupied]
    move = choice(available) if available else None

    thinking.set()
    thread.join()

    return move

def difficult(size:int, delay:int, occupied:list[int] = []) -> int:

    thinking = Event()

    thinking.clear()
    thread = Thread(target=think, args=(thinking,))
    thread.start()

    sleep(delay)

    all_cells = list(range(1, size**2 + 1))
    available = [cell for cell in all_cells if cell not in occupied]
    move = choice(available) if available else None

    thinking.set()
    thread.join()

    return move
