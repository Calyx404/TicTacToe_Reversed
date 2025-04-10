from time import ctime

log_filepath = r'..\logs\game.log'

def log(activity:str) -> None:
    with open(log_filepath, mode = "a", newline = "") as logbook:
        log = logbook.write(f'[{ctime()}] Log : {activity}')
