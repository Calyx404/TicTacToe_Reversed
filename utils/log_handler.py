from datetime import datetime

log_filepath = r'.\logs\game.log'

def log(level:str, activity:str) -> None:

    with open(log_filepath, mode = "a") as logbook:
        log = logbook.write(f'[{datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')}] [{level.upper()}] : {activity}\n')
