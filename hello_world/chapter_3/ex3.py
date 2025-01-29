def generate_fibonacci_sequence(n):
    terms = [0, 1]

    if n == 1:
        return [0]
    if n == 2:
        return terms
    
    while len(terms) < n:
        prev_term_1 = terms[-1]
        prev_term_2 = terms[-2]
        next_term = prev_term_1 + prev_term_2
        terms.append(next_term)

    return terms

def get_nth_fibonacci_term(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    prev_term_1 = get_nth_fibonacci_term(n - 1)
    prev_term_2 = get_nth_fibonacci_term(n - 2)
    return prev_term_1 + prev_term_2