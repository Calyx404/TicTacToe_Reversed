from time import sleep

def load(width:int = 132):

    animation = ['/', '-', '\\', '|']

    for bar in range(1, (width - 1)):

        for state in animation:
            print(f'[{f'{state}{"|" * (bar // 2 - 8)} Loading Game {"|" * (bar // 2 - 8)}{state}' :^{width - 2}}]', end = '\r', flush = True)
            sleep(0.01)

    sleep(1)
