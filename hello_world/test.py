from ex1 import check_if_symmetric
from ex2 import convert_to_numbers
from ex3 import convert_to_letters
from ex4 import get_intersection
from ex5 import get_union
from ex6 import count_characters
from ex7 import is_prime

tests = [
    {
        'function': check_if_symmetric,
        'input': 'racecar',
        'output': True
    },
    {
        'function': check_if_symmetric,
        'input': 'batman',
        'output': False
    },
    {
        'function': check_if_symmetric,
        'input': '',
        'output': True  # An empty string is considered symmetric
    },
    {
        'function': check_if_symmetric,
        'input': 'a',
        'output': True  # A single character is symmetric
    },
    {
        'function': check_if_symmetric,
        'input': 'Aba',
        'output': True  # Case insensitive check
    },
    {
        'function': check_if_symmetric,
        'input': 'abBA',
        'output': True  # Case insensitive check
    },
    {
        'function': check_if_symmetric,
        'input': 'abcd',
        'output': False  # Not a palindrome
    },
    {
        'function': check_if_symmetric,
        'input': 'A man a plan a canal Panama',
        'output': False  # Spaces are considered, not a palindrome
    },
    {
        'function': check_if_symmetric,
        'input': 'No lemon, no melon',
        'output': False  # Punctuation and spaces are considered, not a palindrome
    },

    # Tests for convert_to_numbers
    {
        'function': convert_to_numbers,
        'input': 'a cat',
        'output': [1, 0, 3, 1, 20]
    },
    {
        'function': convert_to_numbers,
        'input': 'hello world',
        'output': [8, 5, 12, 12, 15, 0, 23, 15, 18, 12, 4]
    },
    {
        'function': convert_to_numbers,
        'input': ' ',
        'output': [0]
    },
    {
        'function': convert_to_numbers,
        'input': 'abc',
        'output': [1, 2, 3]
    },
    {
        'function': convert_to_numbers,
        'input': 'zoo',
        'output': [26, 15, 15]
    },
    {
        'function': convert_to_numbers,
        'input': 'a b c',
        'output': [1, 0, 2, 0, 3]
    },

    #Test for convert_to_letters
    {
        'function': convert_to_letters,
        'input': [1, 0, 3, 1, 20],
        'output': 'a cat'
    },
    {
        'function': convert_to_letters,
        'input': [8, 5, 12, 12, 15, 0, 23, 15, 18, 12, 4],
        'output': 'hello world'
    },
    {
        'function': convert_to_letters,
        'input': [0],
        'output': ' '
    },
    {
        'function': convert_to_letters,
        'input': [1, 2, 3],
        'output': 'abc'
    },
    {
        'function': convert_to_letters,
        'input': [26, 15, 15],
        'output': 'zoo'
    },
    {
        'function': convert_to_letters,
        'input': [1, 0, 2, 0, 3],
        'output': 'a b c'
    },

    # Tests for get_intersection
    {
        'function': get_intersection,
        'input': ([1, 2, 3], [2, 3, 4]),
        'output': [2, 3]
    },
    {
        'function': get_intersection,
        'input': ([1, 2, 2, 3], [2, 2, 3, 4]),
        'output': [2, 3]
    },
    {
        'function': get_intersection,
        'input': ([1, 2, 3], [4, 5, 6]),
        'output': []
    },
    {
        'function': get_intersection,
        'input': ([], [1, 2, 3]),
        'output': []
    },
    {
        'function': get_intersection,
        'input': ([1, 2, 3], []),
        'output': []
    },
    {
        'function': get_intersection,
        'input': ([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]),
        'output': [3, 4, 5]
    },

    # Tests for get_union
    {
        'function': get_union,
        'input': ([1, 2, 3], [2, 3, 4]),
        'output': [1, 2, 3, 4]
    },
    {
        'function': get_union,
        'input': ([1, 2, 2, 3], [2, 2, 3, 4]),
        'output': [1, 2, 3, 4]
    },
    {
        'function': get_union,
        'input': ([1, 2, 3], [4, 5, 6]),
        'output': [1, 2, 3, 4, 5, 6]
    },
    {
        'function': get_union,
        'input': ([], [1, 2, 3]),
        'output': [1, 2, 3]
    },
    {
        'function': get_union,
        'input': ([1, 2, 3], []),
        'output': [1, 2, 3]
    },
    {
        'function': get_union,
        'input': ([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]),
        'output': [1, 2, 3, 4, 5, 6, 7]
    },

    # Tests for count_characters
    {
        'function': count_characters,
        'input': 'A cat!!!',
        'output': {'a': 2, 'c': 1, 't': 1, ' ': 1, '!': 3}
    },
    {
        'function': count_characters,
        'input': 'Hello World',
        'output': {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
    },
    {
        'function': count_characters,
        'input': '123 123',
        'output': {'1': 2, '2': 2, '3': 2, ' ': 1}
    },
    {
        'function': count_characters,
        'input': '!!!',
        'output': {'!': 3}
    },
    {
        'function': count_characters,
        'input': '',
        'output': {}
    },
    {
        'function': count_characters,
        'input': 'aAaA',
        'output': {'a': 4}
    },

    # Tests for is_prime
    {
        'function': is_prime,
        'input': 2,
        'output': True  # 2 is the smallest prime number
    },
    {
        'function': is_prime,
        'input': 3,
        'output': True  # 3 is a prime number
    },
    {
        'function': is_prime,
        'input': 4,
        'output': False  # 4 is not a prime number (divisible by 2)
    },
    {
        'function': is_prime,
        'input': 17,
        'output': True  # 17 is a prime number
    },
    {
        'function': is_prime,
        'input': 18,
        'output': False  # 18 is not a prime number (divisible by 2, 3, 6, 9)
    },
    {
        'function': is_prime,
        'input': 19,
        'output': True  # 19 is a prime number
    },
    {
        'function': is_prime,
        'input': 20,
        'output': False  # 20 is not a prime number (divisible by 2, 4, 5, 10)
    },
    {
        'function': is_prime,
        'input': 1,
        'output': False  # 1 is not greater than 1, hence not a prime number
    }
]

num_successes = 0
num_failures = 0

for test in tests:
    function = test['function']
    test_input = test['input']
    desired_output = test['output']
    
    # Check if the input is a tuple (for functions that take multiple arguments)
    if isinstance(test_input, tuple):
        actual_output = function(*test_input)
    else:
        actual_output = function(test_input)
    
    if actual_output == desired_output:
        num_successes += 1
    else:
        num_failures += 1
        function_name = function.__name__
        print('')
        print(f'{function_name} failed on input {test_input}')
        print(f'\tActual output: {actual_output}')
        print(f'\tDesired output: {desired_output}')
print(f'Testing complete: {num_successes} successes and {num_failures} failures.')