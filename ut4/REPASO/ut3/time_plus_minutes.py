# *****************
# FICHO CUANDO TOCA
# *****************


def run(time: str, offset: int) -> str:
    hour = int(time.split(":")[0])
    minutes = int(time.split(":")[1])
    hour_offset = offset//60
    minutes_offset = offset%60
    if hour + hour_offset > 24:
        hour = -1
    if minutes + minutes_offset > 60:
        minutes = minutes_offset - (60 - minutes)
        return f'{hour+hour_offset}:{minutes}'
    final_time = f'{hour+hour_offset}:{minutes+minutes_offset}'
    return final_time


if __name__ == '__main__':
    run('22:55', 315)