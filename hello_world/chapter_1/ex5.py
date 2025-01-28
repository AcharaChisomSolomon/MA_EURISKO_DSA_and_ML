def get_union(array1, array2):
    output = []

    for value in array1:
        if value not in output:
            output.append(value)

    for value in array2:
        if value not in output:
            output.append(value)

    return output