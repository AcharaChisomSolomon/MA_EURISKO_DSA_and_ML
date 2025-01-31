import random

def random_draw(distribution):
    cumulative_distribution = []
    cumulative_sum = 0
    for prob in distribution:
        cumulative_sum += prob
        cumulative_distribution.append(cumulative_sum)

    r = random.random()

    for i, value in enumerate(cumulative_distribution):
        if r <= value:
            return i
