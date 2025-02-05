from backtrack import print_square

def is_valid(square, n):
    num_rows = len(square)
    arrs = (square # rows
    + [list(arr) for arr in zip(*square)] # columns
    + [[square[i][i] for i in range(len(square))]] # main diagonal
    + [[square[i][num_rows-i-1] for i in range(num_rows)]] # opposite diagonal
    )
        
    return all(sum(arr) == n for arr in arrs if None not in arr)

def arr_to_square(arr):
    side_length = int(len(arr) ** 0.5)
    return [arr[i:i+side_length] for i in range(0, len(arr), side_length)]

def get_magic_const(side_length):
    return side_length*(side_length**2+1)/2

def gen_magic_square(size):
    n = get_magic_const(size)
    square = [None for i in range(size**2)]

    current_index = 0
    while None in square or not is_valid(arr_to_square(square), n):
        if square[current_index] == None:
            square[current_index] = 0
        square[current_index] += 1

        if square.count(square[current_index]) > 1:
            continue

        if square[current_index] >= len(square)+1:
            square[current_index] = None
            current_index -= 1
            continue

        if is_valid(arr_to_square(square), n):
            current_index += 1
            
    return arr_to_square(square)

# print_square(gen_magic_square(4))
# print(is_valid(arr_to_square([None] * 9), 15))