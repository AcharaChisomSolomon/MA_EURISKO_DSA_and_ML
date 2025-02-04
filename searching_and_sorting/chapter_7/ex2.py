def isValid(nums):
    for num in nums:
        if num < 0 or num > 26 or int(num) != num:
            return False
    return True

def decode_numbers(numbers, a, b):
    values = [(number - b) / a for number in numbers]
    if not isValid(values):
        return False
    return ''.join([
        chr(97 + int(value) - 1) 
        if value != 0 else ' ' 
        for value in values
        ])
