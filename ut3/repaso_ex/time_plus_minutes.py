# *****************
# FICHO CUANDO TOCA
# *****************


def run(time: str, offset: int) -> str:
    div_time = time.split(":")
    hour = int(div_time[0])
    minutes = int(div_time[1])
    LIMIT_HOUR = 24
    LIMIT_MINUTES = 60

    full_hour = hour + (offset // 60)
    full_minutes = minutes + (offset % 60)

    if full_hour > LIMIT_HOUR:
        full_hour -= LIMIT_HOUR

    if full_minutes > LIMIT_MINUTES:
        full_hour += full_minutes // 60
        full_minutes = full_minutes % 60

    final_time = f"{full_hour}:{full_minutes:02d}"

    return final_time


if __name__ == "__main__":
    run("22:55", 6)
