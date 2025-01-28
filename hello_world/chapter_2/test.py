from ex1 import binary_to_decimal
from ex2 import hexadecimal_to_decimal

tests = [
    # Tests for binary to decimal
    {
        'function': binary_to_decimal,
        'input': '11010',
        'output': '26'
    },
    {
        'function': binary_to_decimal,
        'input': '0',
        'output': '0'
    },
    {
        'function': binary_to_decimal,
        'input': '1',
        'output': '1'
    },
    {
        'function': binary_to_decimal,
        'input': '101',
        'output': '5'
    },
    {
        'function': binary_to_decimal,
        'input': '11111111',
        'output': '255'
    },
    {
        'function': binary_to_decimal,
        'input': '100000',
        'output': '32'
    },

    # Tests for hexadecimal to decimal
    {
        'function': hexadecimal_to_decimal,
        'input': '1A',
        'output': '26'
    },
    {
        'function': hexadecimal_to_decimal,
        'input': '0',
        'output': '0'
    },
    {
        'function': hexadecimal_to_decimal,
        'input': 'F',
        'output': '15'
    },
    {
        'function': hexadecimal_to_decimal,
        'input': '10',
        'output': '16'
    },
    {
        'function': hexadecimal_to_decimal,
        'input': 'FF',
        'output': '255'
    },
    {
        'function': hexadecimal_to_decimal,
        'input': '100',
        'output': '256'
    }
]

num_successes = 0
num_failures = 0

for test in tests:
    function = test['function']
    test_input = test['input']
    desired_output = test['output']
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