def heapify(arr, n, i):
    """
    Function to maintain the max-heap property.
    :param arr: list of integers
    :param n: size of the heap
    :param i: index of the current node
    """
    largest = i         # Initialize largest as root
    left = 2 * i + 1    # Left child index
    right = 2 * i + 2   # Right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        # Recursively heapify the affected subtree
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Function to perform Heap Sort using Max-Heap.
    :param arr: list of integers
    :return: sorted list (ascending order)
    """
    n = len(arr)

    print("🔹 Step 1: Building Max-Heap...")
    # Build a maxheap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    print("   Max-Heap formed:", arr)

    print("\n🔹 Step 2: Extract elements one by one from the heap...")
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root (largest) to end
        arr[i], arr[0] = arr[0], arr[i]
        print(f"   Swap max element {arr[i]} to position {i}: {arr}")

        # Call heapify on the reduced heap
        heapify(arr, i, 0)
        print(f"   Heap after removing element {arr[i]}: {arr[:i]} | Sorted part: {arr[i:]}")

    print("\n✅ Sorted array (Ascending Order):", arr)
    return arr


# -------------------------------------------------------------
# Example Demonstration
# -------------------------------------------------------------
if __name__ == "__main__":
    arr = [45, 12, 89, 33, 25, 77, 5]
    print("Original Array:", arr)
    sorted_arr = heap_sort(arr)





#  Experiment No.: 6
# Title: Design and implement the Heap Sort algorithm to efficiently sort an array of integers
# in ascending order.
# Problem Statement:
# Design and implement a program that uses the Heap Sort algorithm to sort an array of
# integers in ascending order. The implementation should demonstrate the concept of heap data
# structures (max-heap or min-heap) and should be optimized for time and space complexity.
# Objectives:
# 1. To understand the concept and working of heap data structures.
# 2. To implement Heap Sort using a Max-Heap.
# 3. To analyze the time and space efficiency of the algorithm.
# 4. To demonstrate the conversion of an unsorted array into a heap and perform sorting.
# Software and Hardware Requirements:
# Software Requirements Hardware Requirements
# Operating System: Windows /
# Linux
# Processor: Intel Core i3 or higher
# Programming Language: C /
# Python
# RAM: Minimum 4 GB
# IDE: Code::Blocks / VS Code /
# PyCharm
# Storage: Minimum 250 MB free space
# Theory:
# A Heap is a special complete binary tree that satisfies the heap property:
# ● In a Max-Heap, each parent node is greater than or equal to its children.
# ● In a Min-Heap, each parent node is smaller than or equal to its children.
# Heap Sort is based on Max-Heap for sorting in ascending order.
# The algorithm works in two major phases:
# 1. Build Max-Heap: Arrange the array into a valid heap.
# 2. Extract Maximum: Swap the root (largest element) with the last element and reduce
# the heap size. Repeat heapify until all elements are sorted.


# Algorithm: Heap Sort (Using Max-Heap)
# HEAP_SORT(arr, n):
#  BUILD_MAX_HEAP(arr, n)
#  for i = n - 1 down to 1:
#  swap(arr[0], arr[i])
#  MAX_HEAPIFY(arr, 0, i)
# BUILD_MAX_HEAP(arr, n):
#  for i = n/2 - 1 down to 0:
#  MAX_HEAPIFY(arr, i, n)
# MAX_HEAPIFY(arr, i, n):
#  left = 2 * i + 1
#  right = 2 * i + 2
#  largest = i
#  if left < n and arr[left] > arr[largest]:
#  largest = left
#  if right < n and arr[right] > arr[largest]:
#  largest = right
#  if largest != i:
#  swap(arr[i], arr[largest])
#  MAX_HEAPIFY(arr, largest, n)
# Observation Table:
# Sr.
# No.
# Input Array Heap Formed (Max-Heap) Sorted Output
# 1 [12, 11, 13, 5, 6, 7] [13, 11, 12, 5, 6, 7] [5, 6, 7, 11, 12, 13]
# 2 [10, 20, 15, 30, 40] [40, 30, 15, 10, 20] [10, 15, 20, 30, 40]
# 3 [5, 1, 9, 2, 8] [9, 8, 5, 2, 1] [1, 2, 5, 8, 9]
# Time and Space Complexity:
# Operation Complexity
# Build Heap O(n)
# Heapify O(log n)
# Total (Heap Sort) O(n log n)
# Space Complexity O(1) (In-place)


# Conclusion:
# Heap Sort uses the binary heap data structure to efficiently sort elements.
# It guarantees O(n log n) performance in all cases, making it suitable for large datasets where
# memory is limited.



# Experiment 06:
# Python Program:
# Design and implement the Heap Sort algorithm to efficiently sort an array of integers in
# ascending order.
# def heapify(arr, n, i):
#  largest = i
#  left = 2 * i + 1
#  right = 2 * i + 2
#  if left < n and arr[left] > arr[largest]:
#  largest = left
#  if right < n and arr[right] > arr[largest]:
#  largest = right
#  if largest != i:
#  arr[i], arr[largest] = arr[largest], arr[i]
#  heapify(arr, n, largest)
# def heapSort(arr):
#  n = len(arr)
#  for i in range(n // 2 - 1, -1, -1):
#  heapify(arr, n, i)
#  for i in range(n - 1, 0, -1):
#  arr[0], arr[i] = arr[i], arr[0]
#  heapify(arr, i, 0)
# if __name__ == "__main__":
#  arr = [12, 11, 13, 5, 6, 7]
#  print("Original array:", arr)
#  heapSort(arr)
#  print("Sorted array:", arr)
# Output:
# Original array: 12 11 13 5 6 7
# Sorted array: 5 6 7 11 12 13
