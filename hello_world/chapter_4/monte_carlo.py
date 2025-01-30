import random
TOTAL_TRIALS = 1000

def sim_probability(num_heads, num_flips):
    num_heads_counter = 0

    for _ in range(TOTAL_TRIALS):
        current_heads_count = 0

        for _ in range(num_flips):
            rand_value = random.choice([0, 1])
            if rand_value == 0:
                current_heads_count += 1

        if current_heads_count == num_heads:
            num_heads_counter += 1

    return num_heads_counter / TOTAL_TRIALS
