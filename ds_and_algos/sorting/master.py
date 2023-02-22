from functools import reduce

arr = [6, 2, 1, 3, 5, 8, 2, 9, 4]

def selection(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

# print('selection:', selection(arr))

def bubble(arr):
    last_unsorted = len(arr)-1
    for i in range(0, last_unsorted):
        if arr[i] > arr[i+1]:
            arr[i+1], arr[i] = arr[i], arr[i+1]
        if i == last_unsorted:
            last_unsorted -= 1
            continue
    return arr

# print('bubble:', bubble(arr))

def insertion(arr):
    for partition in range(1, len(arr)):
        for i in range(partition, 0, -1):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
    return arr

# print('insertion:', insertion(arr))

def merge(arr, start, end):
    # base case
    if start == end:
        return arr[start]
    # split
    mid = (start+end)//2
    # left
    merge(arr, start, mid)
    # right 
    merge(arr, mid+1, end)
    # merge
    aux = []
    i = start # left pointer
    j = mid+1 # right pointer
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            aux.append(arr[i])
            i += 1
        else:
            aux.append(arr[j])
            j += 1
    while i <= mid:
        aux.append(arr[i])
        i += 1
    while j<= end:
        aux.append(arr[j])
        j += 1
    # copy aux into arr element by element 
    arr[start:end+1] = aux
    return arr

# print('merge:', merge(arr, 0, len(arr)-1))

def quick(arr, start, end):
    if start >= end: return
    pivot = arr[end]
    partition = start
    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[partition] = arr[partition], arr[i]
            partition += 1
    arr[partition], arr[end] = arr[end], arr[partition]
    quick(arr, start, partition-1)
    quick(arr, partition+1, end)
    return arr

# print('quick:', quick(arr, 0, len(arr)-1))

def counting(arr, _range=[1,9]):

    counting_arr = [0]*(_range[1]+1)

    for val in arr:
        counting_arr[val] += 1
    
    for i in range(1, len(counting_arr)):
        counting_arr[i] += counting_arr[i-1]

    aux = [None]*(len(arr)+1)
    for val in arr:
        aux[counting_arr[val]] = val
        counting_arr[val] -= 1

    return aux[_range[0]:]

# print('counting:', counting(arr, _range=[1,9]))

def radix(arr, max_digits):
    for digit in range(max_digits):
        buckets = [[] for i in range(10)]
        for num in arr:
            bucket = num//(10**(digit))%10
            buckets[bucket].append(num)
        arr = reduce(lambda x,y: x+y, buckets)
    return arr

print('radix:', radix(arr=[172, 306, 92, 58, 12, 420, 159, 6], max_digits=3))
