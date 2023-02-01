import random
import time

import algorithms.optimal_knapsack
import algorithms.greedy_knapsack
import algorithms.optimized_dantzing

# Variables
random_values = [1, 100]
random_weights = [1, 100]

# Functions
def generate_random_items(rand_values, rand_weights, len=10):
    items = []
    for i in range(len):
        items.append(
            (random.randint(rand_values[0], rand_values[1]), random.randint(rand_weights[0], rand_weights[1]))
        )

    capacity = random.randint(5, 100)
    return items, capacity

def solve_given_knapsack(items, capacity, verbose=False):
    total_value = algorithms.optimal_knapsack.solve_knapsack(items, capacity)
    greedy_knapsack, greedy_value, greedy_weight = algorithms.greedy_knapsack.solve_knapsack(items, capacity)
    optimal_knapsack, optimal_value, optimal_weight = algorithms.optimized_dantzing.solve_knapsack(items, capacity)

    # Verbose Results
    if verbose:
        print('-----------------[INFO]-----------------')
        print(f'Items: {items}')
        print(f'Knapsack capacity: {capacity}')

        print('\n-----------------[OPTIMAL]-----------------')
        print(f'Total value: {total_value}')

        print('\n-----------------[DANTZING]-----------------')
        print(f'Knapsack contents: {greedy_knapsack}')
        print(f'Total value: {greedy_value}')
        print(f'Total weight: {greedy_weight}')

        print('\n-----------------[OPTIMIZED DANTZING]-----------------')
        print(f'Knapsack contents: {optimal_knapsack}')
        print(f'Total value: {optimal_value}')
        print(f'Total weight: {optimal_weight}')


# Setup
run_iterations = 1000
optimal_better_cnt = 0

start = time.process_time_ns()
for i in range(run_iterations):
    items, capacity = generate_random_items(random_values, random_weights, 10)
    was_optimal_better = solve_given_knapsack(items, capacity)

    if was_optimal_better == 2:
        optimal_better_cnt += 1

print('-----------------[RUN STATS]-----------------')
print(f'Run iterations: {run_iterations}')
print(f'Iterations in which optimal algorithm was better: {optimal_better_cnt}')
print(f"Iterations time: {(time.process_time_ns() - start) / 1e+6}ms")