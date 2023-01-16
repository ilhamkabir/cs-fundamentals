from pprint import pprint
from functools import reduce

def binary_strings_iterative(n=3):
    result = ['0', '1']
    # TODO: review order of loops
    for i in range(1, n):
        temp = []
        for num in result:
            temp.append(num+"0")
            temp.append(num+"1")
        result = temp[:]
    return result

r = binary_strings_iterative()
pprint(r)

def binary_strings(n=3):
    result = []
    def f(n=n, slate=''):
        if n == 0:
            # TODO: review: slate is still string 
            result.append(slate)
        else:
            f(n-1, slate+'0')
            f(n-1, slate+'1')
    f()
    return result

r = binary_strings()
pprint(r)