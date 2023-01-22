import algorithms.basic_knapsack
import algorithms.greedy_knapsack

# Vars
items = [(60, 10), (100, 20), (120, 30)]
capacity = 50

total_value = algorithms.basic_knapsack.solve_knapsack(items, capacity)
print('-----------------[Basic]-----------------')
print("Total value:", total_value)

knapsack, total_value = algorithms.greedy_knapsack.solve_knapsack(items, capacity)
print('\n-----------------[Greedy]-----------------')
print("Knapsack contents:", knapsack)
print("Total value:", total_value)