def int_input(text: str = "") -> int:
    try:
        value = int(input(text))
    except ValueError:
        value = int_input(text)

    return value