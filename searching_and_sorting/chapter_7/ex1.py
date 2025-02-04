def encode_string(string, a, b):
    return [
        (a * (ord(char) - ord('a') + 1)) + b 
        if char.isalpha() else b 
        for char in string
        ]
