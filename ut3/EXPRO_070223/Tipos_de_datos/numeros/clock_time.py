# *********************
# CONTANDO MILISEGUNDOS
# *********************


def run(hours: int, minutes: int, seconds: int) -> float:
    # TU C�DIGO AQU�
    hours_mil = hours*3600*1000
    minutes_mil = minutes*60*1000
    seconds_mil = seconds*1000
    time_since_midnight = hours_mil + minutes_mil + seconds_mil
    return time_since_midnight


if __name__ == '__main__':
    run(0, 1, 1)