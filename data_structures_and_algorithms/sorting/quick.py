"""
Divide-and-conquer
worst (pivot is always one of the bounds): O(n^2)
average case (if pivot is chose correctly): O(nlogn)

Tip for choosing pivot: median-of-three

Step 1: Choose pivot
Step 2: iter thru list, swap all #s < pivot w/ pivot
Step 3: Repeat w/ sublist left of pivot 
Step 4: Repeat w/ sublist right of pivot 
"""

# def quick_sort(array, start_indx, end_indx):
#     if start_indx >= end_indx:
#         return

#     # partition
#     pivot = array[end_indx]
#     p_indx = start_indx # partition index

#     for i in range(start_indx, end_indx-1): # end-1 b/c last index is the pivot 
#         if array[i] <= pivot:
#             tmp = array[i]
#             array[i] = array[p_indx]
#             array[p_indx] = tmp
#             p_indx += 1

#     array[end_indx] = array[p_indx]
#     array[p_indx] = pivot

#     # sort left and right of partition
#     quick_sort(array, start_indx, p_indx-1) # left
#     quick_sort(array, p_indx+1, end_indx) # right

#     return array
    
def quick_sort(array, start, end):

    if start >= end:
        return array
    
    pivot = array[end]
    partition = start

    for i in range(start, end):
        if array[i] <= pivot:
            array[partition], array[i] = array[i], array[partition]
            partition += 1
    
    array[partition], array[end] = array[end], array[partition]

    # left
    quick_sort(array, start, partition-1)
    # right
    quick_sort(array, partition+1, end)

    return array

array = [6, 2, 1, 7, 3, 5, 8, 2, 9, 4]
sorted_array = quick_sort(array, 0, len(array)-1)
print(sorted_array)

# output:
# [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]