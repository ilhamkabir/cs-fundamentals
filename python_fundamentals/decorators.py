# -------- Decorators ----------

# def func_decorator(f):
#     print('tracker')
#     return f

# @func_decorator
# def decorate_func():
#     print('run')

# # tracker runs without needing to call decorate_func
# # makes sense for function registries

# decorate_func()
# decorate_func()
# decorate_func()

# tracker only called once. 


# class Trace:
#     def __init__(self):
#         self.enabled = True

#     # when constructing class is called
#     def __call__(self, f):
#         def wrap(*args, **kwargs):
#             if self.enabled:
#                 print('Calling {}'. format(f))
#             return f(*args, **kwargs)
#         return wrap

# tracer = Trace() #() doesn't call the class, just constructs it.

# @tracer
# def rotate_list(l):
#     return l[1:] + [l[0]]

# l=[1,2,3]

# rotate_list(l)
# rotate_list(l)
# rotate_list(l)

# tracer.enabled = False

# rotate_list(l)
# rotate_list(l)
# rotate_list(l)

# ------------------

class ClassDecorator:
    counter = 0 # class attribute, not instance attribute
    def __init__(self, f): # instead of f: *args, **kwargs
        print('Initialized')

    def __call__(self, f):
        ClassDecorator.counter += 1
        print('Called:', ClassDecorator.counter)
        f() # prints "Class Instance" from here
        return f

# @ClassDecorator
# def decorate_class():
#     # does not run __call__
#     print("Class")

@ClassDecorator()
def decorate_class_instance():
    print("Class Instance")

# @ClassDecorator()
# def decorate_class_instance():
#     print("Class Instance")

# # calling calls __call__(f). need to pass in function
# decorate_class() 

# decorate_class_instance()
# decorate_class_instance()
# decorate_class_instance()

# # ---- getter / setters ----

# class SampleClass:
#     def __init__(self, x):
#         self._x = x

#     @property
#     def x(self):
#         return self._x

#     @x.setter
#     def x(self, value):
#         self._x = value

# s = SampleClass(5)
# print(s.x)
# s.x = 7
# print(s.x)

# def logger(f):
#     def wrapper(*args, **kwargs):
#         print("Running", f.__name__)
#         return f(*args, **kwargs)
#     return wrapper

# @logger
# def add(a,b): return a + b

# x = add(1,4)
# print(x)

# ------------------------------

# class Child:

#     def __init__(self, val):
#         self.some_val = val

#     @staticmethod
#     def static_method():
#         print('static method')

#     @classmethod
#     def class_method(cls):
#         print('class method')


# methods = Child('abc')
# Child.static_method()
# Child.class_method()

# # ------------------

# def check_non_negative(index):
#     def validator(f):
#         def wrap(*args):
#             if args[index] < 0:
#                 raise ValueError
#             return f(*args)
#         return wrap
#     return validator

# # decorator must be callable. check_non_negative is already called
# @check_non_negative(1) #not a decorator but gets a decorator
# def create_list(value, size):
#     return [value]*size
    
# x = create_list(-1,5)
# print(x)
