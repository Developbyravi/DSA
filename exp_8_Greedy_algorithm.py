class Item:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit
        self.ratio = profit / weight  # Profit-to-weight ratio


def fractional_knapsack(items, capacity):
    """
    Function to maximize profit using the Fractional Knapsack approach.
    :param items: list of Item objects (weight, profit)
    :param capacity: maximum weight truck can carry
    :return: maximum profit achievable
    """
    # Step 1: Sort items based on profit/weight ratio (descending)
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_profit = 0.0
    remaining_capacity = capacity

    print(f"Truck Capacity: {capacity} kg")
    print("------------------------------------------------")
    print("Item\tWeight\tProfit\tProfit/Weight")
    for i, item in enumerate(items, start=1):
        print(f"{i}\t{item.weight}\t{item.profit}\t{item.ratio:.2f}")
    print("------------------------------------------------")

    # Step 2: Pick items greedily
    for item in items:
        if remaining_capacity == 0:
            break

        # If item can fit completely, take it
        if item.weight <= remaining_capacity:
            total_profit += item.profit
            remaining_capacity -= item.weight
            print(f"Took full item (Weight={item.weight}, Profit={item.profit})")
        else:
            # Take only the fraction that fits
            fraction = remaining_capacity / item.weight
            total_profit += item.profit * fraction
            print(f"Took {fraction*100:.1f}% of item (Weight={remaining_capacity}, Profit={item.profit * fraction:.2f})")
            remaining_capacity = 0  # Knapsack is full

    print("------------------------------------------------")
    print(f"💰 Maximum Profit = {total_profit:.2f}")
    return total_profit


# ---------------------------------------------------------------
# Example: Shipping Company Parcels
# ---------------------------------------------------------------
if __name__ == "__main__":
    # Each parcel has a weight (kg) and profit (₹)
    parcels = [
        Item(10, 60),   # Parcel 1
        Item(20, 100),  # Parcel 2
        Item(30, 120)   # Parcel 3
    ]

    truck_capacity = 50  # Truck can carry max 50 kg
    fractional_knapsack(parcels, truck_capacity)




#  Experiment No.: 8
# Title:
# Greedy Algorithm (Fractional Knapsack) – CO1, CO2, CO5
# Problem Statement:
# You run a shipping company and need to load a truck with parcels of different weights and
# profits.
# The truck has a limited weight capacity.
# Write a program to choose parcels (even partially) to maximize total profit using the
# Fractional Knapsack strategy.
# Theory:
# The Fractional Knapsack Problem is a Greedy Algorithm problem.
# It aims to achieve the maximum profit for a given weight capacity of the knapsack (truck)
# by selecting items based on their profit-to-weight ratio.
# Unlike the 0/1 Knapsack problem, where items must be completely included or excluded,
# in the Fractional Knapsack, items can be divided into fractions — meaning a part of an
# item can be taken to maximize profit.
# Steps of the Algorithm:
# 1. Compute profit/weight ratio for each item.
# 2. Sort all items in descending order of this ratio.
# 3. Start picking items from the top of the sorted list until the knapsack is full.
# 4. If an item cannot be picked completely, take the fraction of it that fits.
# Algorithm:
# FRACTIONAL_KNAPSACK(weights, profits, capacity):
#  for each item i:
#  ratio[i] = profits[i] / weights[i]
#  Sort items by ratio in descending order
#  total_profit = 0
#  for i in range(n):
#  if weights[i] <= capacity:
#  capacity -= weights[i]
#  total_profit += profits[i]
#  else:
#  fraction = capacity / weights[i]

#  total_profit += profits[i] * fraction
#  break
#  return total_profit


# Experiment 08:Greedy Algorithm (Fractional Knapsack)
# Python Program:
# def fractionalKnapsack(weights, profits, capacity):
#  n = len(weights)
#  ratio = [(profits[i] / weights[i], weights[i], profits[i]) for i in range(n)]
#  # Sort by profit/weight ratio in descending order
#  ratio.sort(reverse=True)
#  total_profit = 0.0
#  for r, w, p in ratio:
#  if capacity >= w:
#  capacity -= w
#  total_profit += p
#  else:
#  fraction = capacity / w
#  total_profit += p * fraction
#  break
#  return total_profit
# # Driver Code
# if __name__ == "__main__":
#  weights = [10, 20, 30]
#  profits = [60, 100, 120]
#  capacity = 50
#  print("Weights:", weights)
#  print("Profits:", profits)
#  print("Truck Capacity:", capacity)
#  max_profit = fractionalKnapsack(weights, profits, capacity)
#  print("Maximum Profit:", max_profit)
# Output:
# Weights: [10, 20, 30]
# Profits: [60, 100, 120]
# Truck Capacity: 50
# Maximum Profit: 240.0