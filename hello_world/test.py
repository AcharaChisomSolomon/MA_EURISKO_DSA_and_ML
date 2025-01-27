from ex1 import check_if_symmetric
from ex2 import convert_to_numbers
from ex3 import convert_to_letters
from ex4 import get_intersection
from ex5 import get_union

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