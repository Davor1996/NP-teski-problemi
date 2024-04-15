import random
import time
import numpy as np

import algorithms.optimal_knapsack
import algorithms.greedy_knapsack
import algorithms.optimized_dantzing

# Functions
def generate_random_items(rand_values, rand_weights, rand_capacity, len=10):
    items = []
    for i in range(len):
        items.append(
            (random.randint(rand_values[0], rand_values[1]), random.randint(rand_weights[0], rand_weights[1]))
        )

    capacity = random.randint(rand_capacity[0], rand_capacity[1])
    return items, capacity

def solve_given_knapsack(items, capacity, verbose=True):

    #print(items)

    optimal_start = time.time_ns()
    optimal_value = algorithms.optimal_knapsack.solve_knapsack(items, capacity)
    optimal_end = time.time_ns()

    greedy_start = time.time_ns()
    greedy_knapsack, greedy_value, greedy_weight = algorithms.greedy_knapsack.solve_knapsack(items, capacity)
    greedy_end = time.time_ns()

    optimized_start = time.time_ns()
    optimized_knapsack, optimized_value, optimized_weight = algorithms.optimized_dantzing.solve_knapsack(items, capacity)
    optimized_end = time.time_ns()

    # Verbose Results
    if verbose:
        print('-----------------[INFO]-----------------')
        print(f'Items: {items}')
        print(f'Knapsack capacity: {capacity}')

        print('\n-----------------[OPTIMAL]-----------------')
        print(f'Total value: {optimal_value}')

        print('\n-----------------[DANTZING]-----------------')
        print(f'Knapsack contents: {greedy_knapsack}')
        print(f'Total value: {greedy_value}')
        print(f'Total weight: {greedy_weight}')

        print('\n-----------------[OPTIMIZED DANTZING]-----------------')
        print(f'Knapsack contents: {optimized_knapsack}')
        print(f'Total value: {optimized_value}')
        print(f'Total weight: {optimized_weight}')

    return greedy_value < optimized_value, optimized_value==optimal_value, (optimal_end - optimal_start), (greedy_end - greedy_start), (optimized_end - optimized_start)

# Variables
random_values = [1, 100]
random_weights = [1, 100]
random_capacity = [5000, 5000]
num_of_items = 2500

# Setup
run_iterations = 1000
optimized_dantzig_better_cnt = 0
optimized_dantzig_optimal_cnt = 0

optimal_list_time_solved = []
greedy_list_time_solved = []
optimized__list_time_solved = []

start = time.time_ns()
for i in range(run_iterations):
    items, capacity = generate_random_items(random_values, random_weights, random_capacity, num_of_items)
    was_optimized_dantzig_better, was_optimized_dantzig_optimal, optimal_time_solved, greedy_time_solved, optimized_time_solved = solve_given_knapsack(items, capacity)

    optimal_list_time_solved.append(optimal_time_solved)
    greedy_list_time_solved.append(greedy_time_solved)
    optimized__list_time_solved.append(optimized_time_solved)

    if was_optimized_dantzig_better:
        optimized_dantzig_better_cnt += 1
    if was_optimized_dantzig_optimal:
        optimized_dantzig_optimal_cnt += 1

    print (f'Iteration: {i+1}')

print('-----------------[RUN STATS]-----------------')
print(f'Run iterations: {run_iterations}')
print(f'Iterations in which optimized dantzig algorithm was better than dantzig algorithm: {optimized_dantzig_better_cnt}')
print(f'Iterations in which optimized dantzig algorithm was optimal: {optimized_dantzig_optimal_cnt}')
print(f"Iterations time: {(time.time_ns() - start) / 1e+6}ms")

print(f'Percentage in which optimized dantzig algorithm was better than dantzig alghoritm: {(optimized_dantzig_better_cnt / run_iterations) * 100}%')
print(f'Percentage in which optimized dantzig algorithm was optimal: {(optimized_dantzig_optimal_cnt / run_iterations) * 100}%' "\n")

print(f"Optimal mean time: {np.mean(optimal_list_time_solved)}ns")
print(f"Greedy mean time: {np.mean(greedy_list_time_solved)}ns")
print(f"Optimized mean time: {np.mean(optimized__list_time_solved)}ns\n")

print(f"Optimal median time: {np.median(optimal_list_time_solved)}ns")
print(f"Greedy median time: {np.median(greedy_list_time_solved)}ns")
print(f"Optimized median time: {np.median(optimized__list_time_solved)}ns\n")

print(f"Optimal time sum: {np.sum(optimal_list_time_solved)}ns")
print(f"Greedy time sum: {np.sum(greedy_list_time_solved)}ns")
print(f"Optimized time sum: {np.sum(optimized__list_time_solved)}ns\n")

print(f"Optimized times: {(greedy_list_time_solved)}")
