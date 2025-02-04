from ex2 import decode_numbers

NUMBERS =  [
    377, 717, 71, 513, 105, 921, 581, 547, 547, 105, 
    377, 717, 241, 71, 105, 547, 71, 377, 547, 717, 
    751, 683, 785, 513, 241, 547, 751
    ]

def get_message():
    print(f'code = {NUMBERS}')
    print(f'potential messages for values between 0 and 100 for a and b => ')
    print()
    for i in range(100 + 1):
        for j in range(100 + 1):
            value = decode_numbers(NUMBERS, i, j)
            if value != False:
                print('=' * len(NUMBERS))
                print(f"\ta = {i} | b = {j}")
                print(f"\tmessage -> {value}")
                print()

