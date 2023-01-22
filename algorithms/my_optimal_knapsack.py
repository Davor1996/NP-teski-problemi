"""
    Solution to the 0/1 Knapsack problem using Dantzing's greedy algorithm.
"""

def solve_knapsack(items, capacity):
    items = sorted(items, key=lambda x: x[0]/x[1], reverse=True)
    heaviest_item = max(items, key=lambda x: x[1])
    items.remove(heaviest_item)
    
    knapsack = []
    total_value = 0
    total_weight = 0
    
    for item in items:
        if total_weight + item[1] <= capacity:
            knapsack.append(item)
            total_value += item[0]
            total_weight += item[1]

    avg_ratio = sum(i[0]/i[1] for i in knapsack) / len(knapsack)
    print(avg_ratio)

    knapsack2 = []
    knapsack2.append(heaviest_item)
    total_value = heaviest_item[0]
    total_weight = heaviest_item[1]

    for item in knapsack:
        if total_weight + item[1] <= capacity:
            knapsack2.append(item)
            total_value += item[0]
            total_weight += item[1]

    return knapsack2, total_value, total_weight, heaviest_item
