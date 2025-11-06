
def merge_sort(orders):
    """
    Function to perform Merge Sort on a list of delivery times.
    :param orders: list of integers representing delivery times in minutes
    :return: sorted list of delivery times (ascending)
    """
    if len(orders) > 1:
        mid = len(orders) // 2  # Divide array into two halves
        left_half = orders[:mid]
        right_half = orders[mid:]

        # Recursive sort for each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge step
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                orders[k] = left_half[i]
                i += 1
            else:
                orders[k] = right_half[j]
                j += 1
            k += 1

        # Copy remaining elements
        while i < len(left_half):
            orders[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            orders[k] = right_half[j]
            j += 1
            k += 1

    return orders


# ---------------------------------------------------------------
# Example: Sorting Online Orders by Delivery Time
# ---------------------------------------------------------------
if __name__ == "__main__":
    # Example input: delivery times in minutes
    delivery_times = [45, 12, 30, 60, 25, 15, 10]
    
    print("🚚 Online Orders - Delivery Times (Unsorted):", delivery_times)
    sorted_orders = merge_sort(delivery_times)
    print("✅ Online Orders Sorted by Delivery Time (Ascending):", sorted_orders)



#  Experiment No.: 7
# Title: Divide and Conquer (Merge Sort) – CO1, CO2, CO5
# Problem Statement:
# You are given a list of online orders, each with an estimated delivery time (in minutes).
# Write a program to sort these orders using the Merge Sort algorithm so that the delivery
# system can prioritize quicker deliveries first.
# Theory:
# Merge Sort is a Divide and Conquer based sorting algorithm.
# It divides the input array into two halves, recursively sorts them, and then merges the two
# sorted halves to produce the final sorted array.
# Steps:
# 1. Divide: Split the array into two halves until each subarray contains one element.
# 2. Conquer: Recursively sort the two halves.
# 3. Combine: Merge the sorted halves to form a single sorted list.
# Key Feature:
# ● Merge Sort is a stable sorting algorithm.
# ● It is efficient for large datasets and ensures O(n log n) performance in all cases.
# Algorithm:
# MERGE_SORT(arr, left, right):
#  if left < right:
#  mid = (left + right) // 2
#  MERGE_SORT(arr, left, mid)
#  MERGE_SORT(arr, mid + 1, right)
#  MERGE(arr, left, mid, right)
# MERGE(arr, left, mid, right):
#  Create subarrays L = arr[left..mid], R = arr[mid+1..right]
#  i, j, k = 0, 0, left
#  while i < len(L) and j < len(R):
#  if L[i] <= R[j]:
#  arr[k] = L[i]
#  i += 1
#  else:
#  arr[k] = R[j]
#  j += 1
#  k += 1
#  Copy remaining elements of L and R (if any)





# Experiment 07:Divide and Conquer (Merge Sort)
# Python Program:
# def merge(arr, left, mid, right):
#  L = arr[left:mid + 1]
#  R = arr[mid + 1:right + 1]
#  i = j = 0
#  k = left
#  while i < len(L) and j < len(R):
#  if L[i] <= R[j]:
#  arr[k] = L[i]
#  i += 1
#  else:
#  arr[k] = R[j]
#  j += 1
#  k += 1
#  # Copy remaining elements
#  while i < len(L):
#  arr[k] = L[i]
#  i += 1
#  k += 1
#  while j < len(R):
#  arr[k] = R[j]
#  j += 1
#  k += 1
# def mergeSort(arr, left, right):
#  if left < right:
#  mid = (left + right) // 2
#  mergeSort(arr, left, mid)
#  mergeSort(arr, mid + 1, right)
#  merge(arr, left, mid, right)
# # Driver Code
# if __name__ == "__main__":
#  delivery_times = [45, 20, 15, 30, 10, 60]
#  print("Original Delivery Times:", delivery_times)
#  mergeSort(delivery_times, 0, len(delivery_times) - 1)
#  print("Sorted by Delivery Time:", delivery_times)

# NAVSAHYADRI EDUCATION SOCIETY’S, GROUP OF INSTITUTIONS
#  Savitribai Phule Pune University
# Second Year of Artificial Intelligence and Machine Learning (2024 Course)
# Course Code: PCC-204-AIM Course Name: Data Structures & Algorithms Lab
# 5 Asst.Prof.Salunkhe A.A
# Output:
# Original Delivery Times: [45, 20, 15, 30, 10, 60]
# Sorted by Delivery Time: [10, 15, 20, 30, 45, 60]