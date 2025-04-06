from time import ctime

log_filepath = r'.\logs\game.log'

def log(activity):
    with open('log.txt', mode = "a", newline = "") as logbook:
        log = logbook.write(f'[{ctime()}] Log : {activity}')
