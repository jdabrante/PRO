# **************************
# BARICENTRO DE UN TRIÁNGULO
# **************************


# def run(A: list, B: list, C: list) -> tuple:
#     x0 = round((A[0] + B[0] + C[0]) / 3, 4)
#     y0 = round((A[1] + B[1] + C[1]) / 3, 4)
#     return x0, y0


def run(A: list, B: list, C: list) -> tuple:

    for i in range(len(A)):
        if i == 0:
            x0 = (A[i] + B[i] + C[i]) / 3
            x0 = round(x0, 4)
        else:
            y0 = (A[i] + B[i] + C[i]) / 3
            y0 = round(y0, 4)

    return x0, y0


if __name__ == "__main__":
    run([4, 6], [12, 4], [10, 10])
