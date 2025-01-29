from ex1 import generate_first_n_recurse1_terms, get_nth_recursive1_term
from ex2 import generate_n_collatz_sequence, get_nth_collatz_sequence
from ex3 import generate_fibonacci_sequence, get_nth_fibonacci_term


tests = [
    {
        'function': generate_first_n_recurse1_terms,
        'input': 1,
        'output': [5]
    },
    {
        'function': generate_first_n_recurse1_terms,
        'input': 2,
        'output': [5, 11]
    },
    {
        'function': generate_first_n_recurse1_terms,
        'input': 3,
        'output': [5, 11, 29]
    },
    {
        'function': generate_first_n_recurse1_terms,
        'input': 4,
        'output': [5, 11, 29, 83]
    },
    {
        'function': generate_first_n_recurse1_terms,
        'input': 5,
        'output': [5, 11, 29, 83, 245]
    },
    {
        'function': get_nth_recursive1_term,
        'input': 1,
        'output': 5
    },
    {
        'function': get_nth_recursive1_term,
        'input': 2,
        'output': 11
    },
    {
        'function': get_nth_recursive1_term,
        'input': 3,
        'output': 29
    },
    {
        'function': get_nth_recursive1_term,
        'input': 4,
        'output': 83
    },
    {
        'function': get_nth_recursive1_term,
        'input': 5,
        'output': 245
    },
    {
        'function': generate_n_collatz_sequence,
        'input': 1,
        'output': [25]
    },
    {
        'function': generate_n_collatz_sequence,
        'input': 2,
        'output': [25, 76]
    },
    {
        'function': generate_n_collatz_sequence,
        'input': 3,
        'output': [25, 76, 38]
    },
    {
        'function': generate_n_collatz_sequence,
        'input': 4,
        'output': [25, 76, 38, 19]
    },
    {
        'function': generate_n_collatz_sequence,
        'input': 5,
        'output': [25, 76, 38, 19, 58]
    },
    {
        'function': get_nth_collatz_sequence,
        'input': 1,
        'output': 25
    },
    {
        'function': get_nth_collatz_sequence,
        'input': 2,
        'output': 76
    },
    {
        'function': get_nth_collatz_sequence,
        'input': 3,
        'output': 38
    },
    {
        'function': get_nth_collatz_sequence,
        'input': 4,
        'output': 19
    },
    {
        'function': get_nth_collatz_sequence,
        'input': 5,
        'output': 58
    },
    {
        'function': generate_fibonacci_sequence,
        'input': 1,
        'output': [0]
    },
    {
        'function': generate_fibonacci_sequence,
        'input': 2,
        'output': [0, 1]
    },
    {
        'function': generate_fibonacci_sequence,
        'input': 3,
        'output': [0, 1, 1]
    },
    {
        'function': generate_fibonacci_sequence,
        'input': 4,
        'output': [0, 1, 1, 2]
    },
    {
        'function': generate_fibonacci_sequence,
        'input': 5,
        'output': [0, 1, 1, 2, 3]
    },
    {
        'function': generate_fibonacci_sequence,
        'input': 6,
        'output': [0, 1, 1, 2, 3, 5]
    },
    {
        'function': get_nth_fibonacci_term,
        'input': 1,
        'output': 0
    },
    {
        'function': get_nth_fibonacci_term,
        'input': 2,
        'output': 1
    },
    {
        'function': get_nth_fibonacci_term,
        'input': 3,
        'output': 1
    },
    {
        'function': get_nth_fibonacci_term,
        'input': 4,
        'output': 2
    },
    {
        'function': get_nth_fibonacci_term,
        'input': 5,
        'output': 3
    },
    {
        'function': get_nth_fibonacci_term,
        'input': 6,
        'output': 5
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