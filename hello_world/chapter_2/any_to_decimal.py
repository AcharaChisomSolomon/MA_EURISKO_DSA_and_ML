def any_base_to_decimal(base, string):
    above_10_dict = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }

    output = 0
    power = len(string) - 1

    for char in string:
        if char in above_10_dict:
            char = above_10_dict[char]
        output += int(char) * (base ** power)
        power -= 1

    return str(output)