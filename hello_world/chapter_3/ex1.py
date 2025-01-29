def generate_first_n_recurse1_terms(n):
    terms = [5]

    while len(terms) < n:
        prev_term = terms[-1]
        next_term = (prev_term * 3) - 4
        terms.append(next_term)

    return terms

def get_nth_recursive1_term(n):
    if n == 1:
        return 5
    
    prev_term = get_nth_recursive1_term(n - 1)
    return (prev_term * 3) - 4