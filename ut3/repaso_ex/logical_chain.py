# ******************
# CALCULADORA LÓGICA
# ******************


# def run(values: list, oper: str) -> bool:
#     last_value = values[0]
#     for value in values:
#         if oper == "and":
#             if last_value == True and value == last_value:
#                 result = True
#             else:
#                 result = False
#         else:
#             if oper == "or":
#                 if last_value == False and value == last_value:
#                     result = False
#                 else:
#                     result = True

#     return result


# if __name__ == "__main__":
#     run([True, True, False], "and")


def run(values: list, oper: str) -> bool:
    last_value = values[0]
    for value in values:
        match oper:
            case "or":
                if value == False and last_value == False:
                    last_value = False
                else:
                    last_value = True
            case "and":
                if value == True and last_value == True:
                    last_value = True
                else:
                    last_value = False
    result = last_value

    return result


if __name__ == "__main__":
    run([True, True, False], "and")
