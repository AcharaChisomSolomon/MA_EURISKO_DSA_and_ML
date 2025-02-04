from ex1 import encode_string
from ex2 import decode_numbers

tests = [
    {
        'function': encode_string,
        'input': ("hello", 2, 3),
        'output': [19, 13, 27, 27, 33]
    },
    {
        'function': encode_string,
        'input': ("world", 1, 0),
        'output': [23, 15, 18, 12, 4]
    },
    {
        'function': encode_string,
        'input': ("test", 3, 1),
        'output': [61, 16, 58, 61]
    },
    {
        'function': encode_string,
        'input': ("encode", 4, 2),
        'output': [22, 58, 14, 62, 18, 22]
    },
    {
        'function': encode_string,
        'input': ("a cat", 2, 3),
        'output': [5, 3, 9, 5, 43]
    },
    {
        'function': decode_numbers,
        'input': ([19, 13, 27, 27, 33], 2, 3),
        'output': "hello"
    },
    {
        'function': decode_numbers,
        'input': ([23, 15, 18, 12, 4], 1, 0),
        'output': "world"
    },
    {
        'function': decode_numbers,
        'input': ([61, 16, 58, 61], 3, 1),
        'output': "test"
    },
    {
        'function': decode_numbers,
        'input': ([22, 58, 14, 62, 18, 22], 4, 2),
        'output': "encode"
    },
    {
        'function': decode_numbers,
        'input': ([5, 3, 9, 5, 43], 2, 3),
        'output': "a cat"
    },
    {
        'function': decode_numbers,
        'input': ([100, 200, 300], 2, 3),
        'output': False  # These numbers do not correspond to a valid message
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