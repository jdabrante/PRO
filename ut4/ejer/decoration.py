def direction_order(direction="asc"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if direction == "asc":
                return sorted(func(*args, **kwargs), reverse=True)
            if direction == "desc":
                return sorted(func(*args, **kwargs))

        return wrapper

    return decorator


@direction_order("asc")
def text2list(text: str) -> list:
    return text.split()


print(text2list("Hola Javier"))
