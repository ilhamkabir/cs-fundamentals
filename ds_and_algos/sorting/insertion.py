"""
O(n^2)
"""

# def insertion_sort(array):
#     for partition in range(len(array)):
#         j = partition-1
#         while j >= 0:
#             if array[partition] < array[j]:
#                 tmp = array[j]
#                 array[j] = array[partition]
#                 array[partition] = tmp
#                 partition = j
#             j -= 1
#     return array

def insertion_sort(arr):
    for partition in range(1, len(arr)):
        for j in range(partition, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

array = [6, 2, 1, 3, 5, 8, 2, 9, 4]
sorted_array = insertion_sort(array)
print(sorted_array)

