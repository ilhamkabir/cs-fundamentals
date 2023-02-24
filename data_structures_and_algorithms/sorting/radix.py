from functools import reduce 

def radix_sort(array, max_digits):
    for digit in range(0, max_digits):
        # create list of 10 empty buckets
        buckets = [[] for i in range(10)]
        for num in array:
            bucket = (num // 10**(digit)) % 10 # take last digit (1 left of decimal)
            buckets[bucket].append(num)
        array = reduce(lambda x, y: x+y, buckets) # or x.extend(y)
    return array

if __name__ == "__main__":
    array = [170, 45, 75, 90, 802, 24, 2, 66]
    sorted_array = radix_sort(array, max_digits=3)
    print(sorted_array)