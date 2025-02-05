from optimal_backtrack import gen_magic_square, print_square

tests = [
    {
        'function': gen_magic_square,
        'input': 3,
        'output': [
            [2,7,6],
            [9,5,1],
            [4,3,8]
        ]
    },
    {
        'function': gen_magic_square,
        'input': 4,
        'output': [
            [1,2,15,16],
            [12,14,3,5],
            [13,7,10,4],
            [8,11,6,9]
        ]
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
        print_square(actual_output)
        num_successes += 1
    else:
        num_failures += 1
        function_name = function.__name__
        print('')
        print(f'{function_name} failed on input {test_input}')
        print(f'\tActual output: {actual_output}')
        print(f'\tDesired output: {desired_output}')
print(f'Testing complete: {num_successes} successes and {num_failures} failures.')
print()
