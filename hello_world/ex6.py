def count_characters(string):
    output = {}

    for char in string:
        if char.lower() in output:
            output[char.lower()] += 1
        else:
            output[char.lower()] = 1

    return output