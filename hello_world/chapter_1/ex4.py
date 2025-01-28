def get_intersection(array1, array2):
    output = []

    for value in array1:
        if value in array2 and value not in output:
            output.append(value)

    return output