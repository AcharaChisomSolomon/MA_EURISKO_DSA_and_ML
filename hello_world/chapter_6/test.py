from cartesian import calc_cartesian_product

tests = [
    {
        'function': calc_cartesian_product,
        'input': [['a'], [1, 2, 3], ['Y', 'Z']],
        'output': [
            ['a', 1, 'Y'],
            ['a', 1, 'Z'],
            ['a', 2, 'Y'],
            ['a', 2, 'Z'],
            ['a', 3, 'Y'],
            ['a', 3, 'Z']
        ]
    },
    {
        'function': calc_cartesian_product,
        'input': [['x', 'y'], [4, 5]],
        'output': [
            ['x', 4],
            ['x', 5],
            ['y', 4],
            ['y', 5]
        ]
    },
    {
        'function': calc_cartesian_product,
        'input': [['p', 'q'], [6], ['A', 'B']],
        'output': [
            ['p', 6, 'A'],
            ['p', 6, 'B'],
            ['q', 6, 'A'],
            ['q', 6, 'B']
        ]
    },
    {
        'function': calc_cartesian_product,
        'input': [[1, 2], [3, 4], [5, 6]],
        'output': [
            [1, 3, 5],
            [1, 3, 6],
            [1, 4, 5],
            [1, 4, 6],
            [2, 3, 5],
            [2, 3, 6],
            [2, 4, 5],
            [2, 4, 6]
        ]
    },
    {
        'function': calc_cartesian_product,
        'input': [[], [1, 2]],
        'output': []
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