"""
functools module is for higher order functions
take functions as arguments, manipulate them, and return them as output
"""

from functools import reduce
import operator 

x = reduce(operator.add, [1,2,3,4,5])
# print(x)

from functools import total_ordering

@total_ordering
class Car:
    def __init__(self, model, mileage):
        self.model = model
        self.mileage = mileage

    def __eq__(self, other):
        return self.mileage == other.mileage

    # must have one. total_ordering will extrapolate for le, gt, ge
    def __lt__(self, other):
        return self.mileage == other.mileage

c1 = Car("BMW", 700)
c2 = Car("Toyota", 700)
c3 = Car("Audi", 900)

# print(c1 == c2)
# print(c1 == c3)
# print(c1 < c2)

from functools import lru_cache # no more cached_property

class Test:
    def __init__(self, grade):
        self._grade = grade

    # @cached_property
    @property
    def grade(self):
        print('calculating...')
        return self._grade

# test = Test(85)
# print(test.grade)
# print(test.grade)

@lru_cache(maxsize=5) #maxsize: # of calls to keep cache for
def fib(n):
    print('n =', n)
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# fib_list = [fib(n) for n in range(10)]
# for n in fib_list: print(n)


from functools import partial 
def add(a,b): return a+b
add_one = partial(add, 1) # positional argument
# print(add_one(b=5)) # keyword argument


from functools import wraps
def logger(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print("Running", f.__name__)
        return f(*args, **kwargs)
    return wrapper

@logger
def add(a,b): 
    """add a and b"""
    return a + b

x = add(1,4)
# print(x)
# print(add.__name__) #without @wraps: wrapper
# print(add.__doc__) #without @wraps: no doc string

from functools import singledispatch

# def append_one(obj):
#     if type(obj) == list:
#         return obj + [1]
#     elif type(obj) == set:
#         return obj.union({1})
#     elif type(obj) == str:
#         return obj + str(1)
#     else:
#         print("Unsupported type")
#         return obj

# print(append_one('asdf '))

@singledispatch
def append_one(obj):
    pass

@append_one.register(str)
def _(obj):
    return obj + str(1)

# print(append_one('asdf '))
