TOTAL = 15
DIGITS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_valid(square):
    return (
        (square[0][0] + square[0][1] + square[0][2] == TOTAL) and 
        (square[1][0] + square[1][1] + square[1][2] == TOTAL) and 
        (square[2][0] + square[2][1] + square[2][2] == TOTAL) and
        (square[0][0] + square[1][0] + square[2][0] == TOTAL) and
        (square[0][1] + square[1][1] + square[2][1] == TOTAL) and
        (square[0][2] + square[1][2] + square[2][2] == TOTAL) and
        (square[0][0] + square[1][1] + square[2][2] == TOTAL) and
        (square[2][0] + square[1][1] + square[0][2] == TOTAL)
    )

def print_square(square):
    print('=' * 9 * 2)
    print(f'\t[[{",".join(list(map(lambda x: str(x), square[0])))}],')
    print(f'\t [{",".join(list(map(lambda x: str(x), square[1])))}],')
    print(f'\t [{",".join(list(map(lambda x: str(x), square[2])))}]]')
    print()

def get_digits(*args):
    new_digits = []
    for digit in DIGITS:
        if digit not in args:
            new_digits.append(digit)
    return new_digits

def all_valid_nums(a, b, c):
    return a != None and b != None and c != None

def is_hopeless(square):
    if all_valid_nums(square[0][0], square[0][1], square[0][2]):
        if square[0][0] + square[0][1] + square[0][2] != TOTAL:
            return True
    if all_valid_nums(square[1][0], square[1][1], square[1][2]):
        if square[1][0] + square[1][1] + square[1][2] != TOTAL:
            return True
    if all_valid_nums(square[2][0], square[2][1], square[2][2]):
        if square[2][0] + square[2][1] + square[2][2] != TOTAL:
            return True
    if all_valid_nums(square[0][0], square[1][0], square[2][0]):
        if square[0][0] + square[1][0] + square[2][0] != TOTAL:
            return True
    if all_valid_nums(square[0][1], square[1][1], square[2][1]):
        if square[0][1] + square[1][1] + square[2][1] != TOTAL:
            return True
    if all_valid_nums(square[0][2], square[1][2], square[2][2]):
        if square[0][2] + square[1][2] + square[2][2] != TOTAL:
            return True
    if all_valid_nums(square[0][0], square[1][1], square[2][2]):
        if square[0][0] + square[1][1] + square[2][2] != TOTAL:
            return True
    if all_valid_nums(square[2][0], square[1][1], square[0][2]):
        if square[2][0] + square[1][1] + square[0][2] != TOTAL:
            return True
    return False

def brute_force():
    print('WITH BRUTEFORCE ===>>>>')
    print()
    permutations = 0
    count = 0
    square = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

    for num1 in DIGITS:
        square = [
            [num1, None, None],
            [None, None, None],
            [None, None, None]
        ]
        for num2 in get_digits(num1):
            square = [
                [num1, num2, None],
                [None, None, None],
                [None, None, None]
            ]
            for num3 in get_digits(num1, num2):
                square = [
                    [num1, num2, num3],
                    [None, None, None],
                    [None, None, None]
                ]
                for num4 in get_digits(num1, num2, num3):
                    square = [
                        [num1, num2, num3],
                        [num4, None, None],
                        [None, None, None]
                    ]
                    for num5 in get_digits(num1, num2, num3, num4):
                        square = [
                            [num1, num2, num3],
                            [num4, num5, None],
                            [None, None, None]
                        ]
                        for num6 in get_digits(num1, num2, num3, num4, num5):
                            square = [
                                [num1, num2, num3],
                                [num4, num5, num6],
                                [None, None, None]
                            ]
                            for num7 in get_digits(num1, num2, num3, num4, num5, num6):
                                square = [
                                    [num1, num2, num3],
                                    [num4, num5, num6],
                                    [num7, None, None]
                                ]
                                for num8 in get_digits(num1, num2, num3, num4, num5, num6, num7):
                                    square = [
                                        [num1, num2, num3],
                                        [num4, num5, num6],
                                        [num7, num8, None]
                                    ]
                                    for num9 in get_digits(num1, num2, num3, num4, num5, num6, num7, num8):
                                        square = [
                                            [num1, num2, num3],
                                            [num4, num5, num6],
                                            [num7, num8, num9]
                                        ]
                                        permutations += 1

                                        if is_valid(square):
                                            count += 1
                                            print(f'gotten at permutation {permutations}')
                                            print_square(square)
                                            
    print(f'Took {permutations} permutations with BRUTEFORCE')
    print(f'Got {count} squares whose rows, columns and diagonals add up to {TOTAL}')

def backtracking():
    print()
    print('WITH BACKTRACKING ===>>>>')
    print()
    permutations = 0
    count = 0
    square = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

    for num1 in DIGITS:
        square = [
            [num1, None, None],
            [None, None, None],
            [None, None, None]
        ]
        if is_hopeless(square):
            continue
        for num2 in get_digits(num1):
            square = [
                [num1, num2, None],
                [None, None, None],
                [None, None, None]
            ]
            if is_hopeless(square):
                continue
            for num3 in get_digits(num1, num2):
                square = [
                    [num1, num2, num3],
                    [None, None, None],
                    [None, None, None]
                ]
                if is_hopeless(square):
                    continue
                for num4 in get_digits(num1, num2, num3):
                    square = [
                        [num1, num2, num3],
                        [num4, None, None],
                        [None, None, None]
                    ]
                    if is_hopeless(square):
                        continue
                    for num5 in get_digits(num1, num2, num3, num4):
                        square = [
                            [num1, num2, num3],
                            [num4, num5, None],
                            [None, None, None]
                        ]
                        if is_hopeless(square):
                            continue
                        for num6 in get_digits(num1, num2, num3, num4, num5):
                            square = [
                                [num1, num2, num3],
                                [num4, num5, num6],
                                [None, None, None]
                            ]
                            if is_hopeless(square):
                                continue
                            for num7 in get_digits(num1, num2, num3, num4, num5, num6):
                                square = [
                                    [num1, num2, num3],
                                    [num4, num5, num6],
                                    [num7, None, None]
                                ]
                                if is_hopeless(square):
                                    continue
                                for num8 in get_digits(num1, num2, num3, num4, num5, num6, num7):
                                    square = [
                                        [num1, num2, num3],
                                        [num4, num5, num6],
                                        [num7, num8, None]
                                    ]
                                    if is_hopeless(square):
                                        continue
                                    for num9 in get_digits(num1, num2, num3, num4, num5, num6, num7, num8):
                                        square = [
                                            [num1, num2, num3],
                                            [num4, num5, num6],
                                            [num7, num8, num9]
                                        ]
                                        if is_hopeless(square):
                                            continue
                                        permutations += 1

                                        if is_valid(square):
                                            count += 1 
                                            print(f'gotten at permutation {permutations}')
                                            print_square(square)
                                            
    print(f'Took {permutations} permutations with BACKTRACKING')
    print(f'Got {count} squares whose rows, columns and diagonals add up to {TOTAL}')

brute_force()
backtracking()