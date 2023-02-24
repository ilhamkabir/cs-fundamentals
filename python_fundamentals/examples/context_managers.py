class Logger:
    def __enter__(self):
        print('enter')

    def __exit__(self, exc_type, exc_val, traceback):
        print('exit')

# with Logger() as x:
#     raise ValueError('## Value Error')

# with open('sample.txt', 'w') as f:
#     f.write('will this override?')

# with open('sample.txt', 'r') as f:
#     print(f.read())

# use for set up and tear down
from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    f = open(file, mode)
    yield f # generator function. doesn't hold entire result in mem, yields one result at a time!
    f.close()

with open_file('sample.txt', 'r') as f:
    print(f.read())

# <generators>

# iterates over whole list, returns whole list
some_list = [1,2,3,4,5,6]

def without_generator(some_list):
    for i in range(len(some_list)):
        some_list[i] *= 2
    return some_list

# returns each item one at a time from the list
def with_generator(some_list):
    for i in range(len(some_list)):
        yield some_list[i]*2

# for item in with_generator(some_list):
#     print(item)

# items = with_generator(some_list)
# for item in items:
#     print(item)

# generator functions
def square_nums(nums):
    for n in nums:
        yield n*n

nums = square_nums([1,2,3,4,5])

# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums)) # throws StopIteration 

# for num in nums:
#     print(num)

# </ generators>

import os

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        # teardown
        os.chdir(cwd)

# with change_dir('Sample-Dir-One'):
#     open('test.txt', 'a').close()
#     # with open('test.txt', mode='a'):
#     #     pass

# with change_dir('Sample-Dir-Two'):
#     open('test.txt', 'a').close()
#     # with open('test.txt', mode='a'):
#     #     pass

# ----------------------------------

# static and class methods

class Child:

    some_val = 123

    def __init__(self, val):
        self.some_val = val

    @staticmethod
    def static_method():
        print('child static method')

    @classmethod
    def class_method(cls):
        print('child class method')
        print(cls.some_val)


child = Child('abc')
child.static_method()
child.class_method()

class Parent(Child):
    def __init__(self, val):
        self.some_val = val

    @staticmethod
    def static_method():
        print('parent static method')

    @classmethod
    def class_method(cls):
        print('parent class method')
        print(cls.some_val)

parent = Parent('xyz')
parent.static_method()
parent.class_method()
