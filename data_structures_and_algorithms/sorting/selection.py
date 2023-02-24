"""
Brute force
O(n^2)

Step 1: Set current index to 0
Step 2: Iterate thru list looking for vals < current index
Step 3: Swap min with current index
Step 4: increment current idx
Step 4: repeat
"""

# def selection_sort(array):
#     for curr_idx in range(len(array)):
#         min_idx = curr_idx + 1
#         while min_idx < len(array):
#             if array[min_idx] < array[curr_idx]:
#                 tmp = array[curr_idx]
#                 array[curr_idx] = array[min_idx]
#                 array[min_idx] = tmp
#             min_idx += 1
#     return array

def selection_sort(array):
    for i in range(len(array)):
        min = i
        for j in range(i+1, len(array)):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
    return array


array = [6, 2, 1, 3, 5, 8, 2, 9, 4]
sorted_array = selection_sort(array)
print(sorted_array)
