# swim club

import statistics

def read_swim_data(fn):
    with open(fn) as file:
        lines = file.readlines()
        times = lines[0].strip().split(',')

    converts = []
    for time in times:
        if ":" in time:
            minutes, rest = time.split(':')
        else:
            minutes = '0'
            rest = time
        seconds, hundredths = rest.split('.')
        converts.append(int(minutes) * 60 * 100 + int(seconds) * 100 + int(hundredths))

    average = statistics.mean(converts)
    rest, hundredths = str(round(average / 100.0, 2)).split('.')
    rest = int(rest)
    minutes = rest // 60
    seconds = rest - minutes * 60

    return str(minutes) + ":" + str(seconds) + "." + str(hundredths)