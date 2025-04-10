from random import choice
from time import sleep
import threading

def move(size: int, delay: int = 2, occupied: list[int] = []) -> int:
    from threading import Thread, Event
    from time import sleep

    thinking = Event()

    def think():
        text = "Bot is thinking..."
        interval = 0.1

        while not thinking.is_set():
            for i in range(1, len(text) + 1):
                if thinking.is_set():
                    break
                print(" " * 50, end="\r")
                print(f"Opponent's turn : {text[:i]}", end="\r", flush=True)
                sleep(interval)
        print(" " * 50, end="\r", flush=True)

    thinking.clear()
    thread = Thread(target=think)
    thread.start()

    sleep(delay)

    all_cells = list(range(1, size**2 + 1))
    available = [cell for cell in all_cells if cell not in occupied]
    move = choice(available) if available else None

    thinking.set()
    thread.join()

    return move
