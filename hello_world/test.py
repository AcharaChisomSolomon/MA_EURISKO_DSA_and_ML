from ex1 import check_if_symmetric

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
    # Edge cases
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