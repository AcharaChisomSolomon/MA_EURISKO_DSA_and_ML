from ex1 import generate_first_n_recurse1_terms, get_nth_recursive1_term


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