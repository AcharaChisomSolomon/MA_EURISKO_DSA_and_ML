from monte_carlo import sim_probability, TOTAL_TRIALS

MIN_NUM_FLIPS = 5
MAX_NUM_FLIPS = 10

GRAPH_UNIT = 15

def get_head_prob_values(num_flips):
    head_values = []
    for i in range(num_flips + 1):
        head_values.append(sim_probability(i, num_flips))
    return head_values

def generate_prob_graph_lsts(num_flips):
    head_values = get_head_prob_values(num_flips)
    head_values = list(map(lambda num: num * TOTAL_TRIALS, head_values))

    graph_lines_lsts = []
    for i in range((int(max(head_values)) // GRAPH_UNIT) + 1):
        graph_lines_lsts.append([])

    for lines_lst in graph_lines_lsts:
        for i in range(len(head_values)):
            prob_value = head_values[i]
            if prob_value > 0:
                lines_lst.append('|')
                head_values[i] -= GRAPH_UNIT
            else:
                lines_lst.append(' ')

    index = len(graph_lines_lsts) - 1
    while index > -1:
        print(' '.join(graph_lines_lsts[index]))
        index -= 1

def display_info(num_flips):
    print('=' * 50)
    head_probs = get_head_prob_values(num_flips)
    print(f"The probabilty of getting 0 - {num_flips} heads in {num_flips} coin flips is shown below =>")
    for i in range(len(head_probs)):
        print(f" - {i} heads => {head_probs[i]}")
    print()
    print(f' Sum of all probabilities = {sum(head_probs):.2f}')

def draw_graphs():
    for i in range(MIN_NUM_FLIPS, MAX_NUM_FLIPS + 1):
        display_info(i)
        print()
        print('The distribution curve(lol) is shown below:')
        generate_prob_graph_lsts(i)
        print()

draw_graphs()
