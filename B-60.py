
import heapq

class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound

    def __lt__(self, other):
        return self.bound > other.bound

def calc_bound(node, n, capacity, wt, val):
    if node.weight >= capacity:
        return 0

    profit_bound = node.profit
    j = node.level + 1
    total_wt = node.weight

    while j < n and total_wt + wt[j] <= capacity:
        total_wt += wt[j]
        profit_bound += val[j]
        j += 1

    if j < n:
        profit_bound += (capacity - total_wt) * val[j] / wt[j]

    return profit_bound

def knapsack(values, weights, capacity):
    n = len(values)

 
    ratio = []
    for i in range(n):
        ratio.append([values[i] / weights[i], values[i], weights[i]])

    # simple sorting (manual key logic removed)
    ratio.sort(reverse=True)

    sorted_values = []
    sorted_weights = []

    for i in range(n):
        sorted_values.append(ratio[i][1])
        sorted_weights.append(ratio[i][2])

    values = sorted_values
    weights = sorted_weights

    pq = []
    root = Node(-1, 0, 0, 0)
    root.bound = calc_bound(root, n, capacity, weights, values)
    heapq.heappush(pq, root)

    max_profit = 0

    while pq:
        node = heapq.heappop(pq)

        if node.bound > max_profit:
            i = node.level + 1

            if i < n:
                
                inc = Node(i,
                           node.profit + values[i],
                           node.weight + weights[i],
                           0)

                if inc.weight <= capacity:
                    max_profit = max(max_profit, inc.profit)

                inc.bound = calc_bound(inc, n, capacity, weights, values)
                if inc.bound > max_profit:
                    heapq.heappush(pq, inc)

                
                exc = Node(i,
                           node.profit,
                           node.weight,
                           0)

                exc.bound = calc_bound(exc, n, capacity, weights, values)
                if exc.bound > max_profit:
                    heapq.heappush(pq, exc)

    return max_profit

# Example
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print("Max Profit:", knapsack(values, weights, capacity))

