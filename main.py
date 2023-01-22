import random

import algorithms.basic_knapsack
import algorithms.greedy_knapsack
import algorithms.my_optimal_knapsack

# Functions
def generate_random_items(rand_values, rand_weights, len=10):
    items = []
    for i in range(len):
        items.append(
            (random.randint(rand_values[0], rand_values[1]), random.randint(rand_weights[0], rand_weights[1]))
        )
    return items

# Variables setup
random_values = [2, 10]
random_weights = [1, 10]

items = generate_random_items(random_values, random_weights, 10)
capacity = random.randint(5, 20)

# Results
print('-----------------[INFO]-----------------')
print(f'Items: {items}')
print(f'Greedy sort: {sorted(items, key=lambda x: x[0]/x[1], reverse=True)}')
print(f'Knapsack capacity: {capacity}')

total_value = algorithms.basic_knapsack.solve_knapsack(items, capacity)
print('\n-----------------[BASIC]-----------------')
print(f'Total value: {total_value}')

knapsack, total_value, total_weight = algorithms.greedy_knapsack.solve_knapsack(items, capacity)
print('\n-----------------[GREEDY]-----------------')
print(f'Knapsack contents: {knapsack}')
print(f'Total value: {total_value}')
print(f'Total weight: {total_weight}')

knapsack, total_value, total_weight, heaviest_item = algorithms.my_optimal_knapsack.solve_knapsack(items, capacity)
print('\n-----------------[MY OPTIMAL]-----------------')
print(f'Knapsack contents: {knapsack}')
print(f'Heaviest item: {heaviest_item}')
print(f'Total value: {total_value}')
print(f'Total weight: {total_weight}')