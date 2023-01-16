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

print('selection:', selection(arr))

def bubble(arr):
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

print('bubble:', bubble(arr))

def insertion(arr):
    for partition in range(1, len(arr)):
        for i in range(partition, 0, -1):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
    return arr
    
print('insertion:', insertion(arr))

def merge(arr, start, end):

    if start >= end:
        return

    mid = (start + end)//2
    merge(arr, start, mid)
    merge(arr, mid+1, end)

    aux = []
    L = start
    R = mid+1

    #TODO: review and
    while L <= mid and R <= end:
        if arr[L] <= arr[R]:
            aux.append(arr[L])
            L += 1
        else:
            aux.append(arr[R])
            R += 1

    if L <= mid:
        aux.extend(arr[L:mid+1])
    if R <= end:
        aux.extend(arr[R:end+1])

    arr[start: end+1] = aux

    return arr

print('merge:', merge(arr, 0, len(arr)-1))

def quick(arr, start, end):
    if start >= end:
        return
    partition = start
    pivot = arr[end]
    for i in range(start, end):
        if arr[i] < pivot:
            partition += 1
        else:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    arr[partition], arr[end] = arr[end], arr[partition]
    quick(arr, start, partition-1)
    quick(arr, partition+1, end)
    return arr

print('quick:', quick(arr, 0, len(arr)-1))

def counting(arr, ceiling):
    counting = [0]*(ceiling+1)

    for num in arr:
        counting[num] += 1

    for i in range(1, len(counting)):
        counting[i] += counting[i-1]

    final = [None]*len(arr)
    for i in range(len(arr)-1, -1, -1):
        #TODO: review arr[i]]-1
        final[counting[arr[i]]-1] = arr[i]
        counting[arr[i]] -= 1
    return arr
    
print('counting:', counting(arr, ceiling=max(arr)))

def radix(arr, max_digits):
    for i in range(1, max_digits):
        buckets = [[] for i in range(10)]
        for num in arr: 
            #TODO: review //
            bucket = (num//(10**i))%10
            buckets[bucket].append(num)
        arr = reduce(lambda x,y: x+y, buckets)
    return arr

print(
    'radix:', 
    radix(arr=[172, 306, 92, 58, 12, 420, 159, 6], 
    max_digits=3)
)


