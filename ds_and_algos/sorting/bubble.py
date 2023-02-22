"""
Brute force
Swap with adjacent
O(n^2)
No extra memory
very last element will be sorted
---
step 1: walk thru array, swap as needed. set "sorted" flag to false if sort needed.
step 2: repeat (to last unsorted) until sorted is true
"""

def bubble_sort(arr):
    last_unsorted = len(arr) - 1
    i = 0
    while i < last_unsorted:
        sorted = True
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            sorted = False
        if i+1 == last_unsorted:
            if sorted: break
            last_unsorted -= 1
            i = 0
        else:
            i += 1
    return arr

array = [6, 2, 1, 3, 5, 8, 2, 9, 4]
sorted_array = bubble_sort(array)
print(sorted_array)
