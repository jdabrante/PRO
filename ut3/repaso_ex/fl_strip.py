# ****************
# TROCEADO EXTREMO
# ****************


# def run(numbers: str) -> str:
# numbers_list = numbers.split(",")

# if numbers_list != [] and (len(numbers_list) > 1):
#     del numbers_list[len(numbers_list) - 1]
#     del numbers_list[0]
# elif numbers_list != []:
#     del numbers_list[0]

# strip_numbers = " ".join(numbers_list)


def run(numbers: str) -> str:
    numbers = numbers.split(",")
    strip_numbers = numbers[1 : len(numbers) - 1]
    strip_numbers = " ".join(strip_numbers)
    return strip_numbers


if __name__ == "__main__":
    run("")
