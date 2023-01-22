import random

import algorithms.basic_knapsack
import algorithms.greedy_knapsack

# Functions
def generate_random_items(rand_values, rand_weights, len=10):
    items = []
    for i in range(len):
        items.append(
            (random.randint(rand_values[0], rand_values[1]), random.randint(rand_weights[0], rand_weights[1]))
        )
    return items

# Variables setup
random_values = [1, 100]
random_weights = [10, 50]

items = generate_random_items(random_values, random_weights, 20)
capacity = random.randint(50, 150)

# Results
print('-----------------[INFO]-----------------')
print(f'Items: {items}')
print(f'Knapsack capacity: {capacity}')

total_value = algorithms.basic_knapsack.solve_knapsack(items, capacity)
print('\n-----------------[BASIC]-----------------')
print(f'Total value: {total_value}')

knapsack, total_value = algorithms.greedy_knapsack.solve_knapsack(items, capacity)
print('\n-----------------[GREEDY]-----------------')
print(f'Knapsack contents: {knapsack}')
print(f'Total value: {total_value}')