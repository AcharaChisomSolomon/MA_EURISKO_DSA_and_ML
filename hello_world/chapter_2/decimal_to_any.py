def decimal_to_any_base(base, string):
    if string == '0':
        return '0'
    
    above_10_dict = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }

    decimal = int(string)
    output = ''

    while decimal > 0:
        remainder = decimal % base
        decimal = decimal // base
        if remainder in above_10_dict:
            remainder = above_10_dict[remainder]
        output = str(remainder) + output

    return output