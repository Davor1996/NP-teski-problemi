"""
    Solution to the 0/1 Knapsack problem using optimized Dantzing's greedy algorithm.
"""

def solve_greedy_knapsack(items, capacity):
    items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)

    knapsack = []
    total_value = 0
    total_weight = 0

    for item in items:
        if total_weight + item[1] <= capacity:
            knapsack.append(item)
            total_value += item[0]
            total_weight += item[1]

    return knapsack, total_value, total_weight

def solve_without_last(items, capacity, knapsack, total_value, total_weight):
    #knapsack = sorted(knapsack, key=lambda x: x[1], reverse=True)
    unique_items = list(set(items) - set(knapsack))
    last_item = knapsack.pop(0)

    total_value -= last_item[0]
    total_weight -= last_item[1]

    for item in unique_items:
        if total_weight + item[1] <= capacity:
            knapsack.append(item)
            total_value += item[0]
            total_weight += item[1]

    return knapsack, total_value, total_weight

def solve_knapsack(items, capacity):
    knapsack, total_value, total_weight = solve_greedy_knapsack(items, capacity)
    if len(knapsack) == 0:
        return [], 0, 0

    optimized_knapsack, optimized_total_value, optimized_total_weight = solve_without_last(items, capacity, knapsack, total_value, total_weight)
    
    if optimized_total_value > total_value:
        return optimized_knapsack, optimized_total_value, optimized_total_weight
    else:
        return knapsack, total_value, total_weight