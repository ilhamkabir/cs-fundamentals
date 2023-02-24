"""
Divide and conquer
O(nlogn)
Lot of memory (new lists)
---
step 1: keep splitting till we have 1 elem in left and right list
step 2: sort & merge
"""

# def merge_sort(array):
#     # step 1: split
#     if len(array) < 2:
#         return array

#     right_start = len(array)//2

#     left_array = array[0: right_start]
#     right_array = array[right_start:]

#     left_array = merge_sort(left_array) # left
#     right_array = merge_sort(right_array) # right

#     # step 2 : sort & merge
#     sorted_array = merge(left_array, right_array)
#     return sorted_array

# def merge(left_array, right_array):
#     sorted_array = []

#     left_idx = 0
#     right_idx = 0

#     while (left_idx < len(left_array) and right_idx < len(right_array)):
#         if left_array[left_idx] <= right_array[right_idx]:
#             sorted_array.append(left_array[left_idx])
#             left_idx += 1
#         else:
#             sorted_array.append(right_array[right_idx])
#             right_idx += 1

#     if left_idx < len(left_array):
#         sorted_array.extend(left_array[left_idx:])

#     if right_idx < len(right_array):
#         sorted_array.extend(right_array[right_idx:])

#     return sorted_array

def merge_sort(array, start, end):
    # base case
    if start == end:
        return array
    # split into 2 halves
    mid = (start+end)//2
    merge_sort(array, start, mid)
    merge_sort(array, mid+1, end)
    # merge 2 sorted halves
    aux = [] # size: end-start+1
    i = start
    j = mid+1
    while i <= mid and j <= end:
        if array[i] <= array[j]:
            aux.append(array[i])
            i += 1
        else:
            aux.append(array[j])
            j += 1
    # append left overs
    while i <= mid:
        aux.append(array[i])
        i += 1
    while j <= end:
        aux.append(array[j])
        j += 1

    # copy back values from aux array to original array element by element
    array[start:end+1] = aux

    return array

array = [6, 2, 1, 3, 5, 8, 2, 9, 4]
# sorted_array = merge_sort(array)
sorted_array = merge_sort(array, 0, len(array)-1)
print(sorted_array)
