def generate_n_collatz_sequence(n):
    terms = [25]

    while len(terms) < n:
        prev_term = terms[-1]

        if prev_term % 2 == 0:
            next_term = prev_term / 2
        else:
            next_term = (prev_term * 3) + 1

        terms.append(next_term)

    return terms


def get_nth_collatz_sequence(n):
    if n == 1:
        return 25
    
    prev_term = get_nth_collatz_sequence(n - 1)

    if prev_term % 2 == 0:
        next_term = prev_term / 2
    else:
        next_term = (prev_term * 3) + 1

    return next_term