def binary_to_decimal(string):
    output = 0
    power = len(string) - 1

    for char in string:
        output += int(char) * (2 ** power)
        power -= 1

    return str(output)