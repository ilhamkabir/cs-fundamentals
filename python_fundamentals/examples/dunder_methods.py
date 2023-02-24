# dunder methods

class Foo:
    def __init__(self, x):
        self.x = x

    def __call__(self, x):
        print('__call__')

# print('init:')
x = Foo(1)
# print('x.x', x.x)
# __init__ doesn't return anything. y=None
# `x` is reinitialized
y = x.__init__(2)
# print('x.x', x.x)

def extended(*args, **kwargs):
    print('args', args)
    print('kwargs', kwargs)

extended(1,2,3, {'A': 'a', 'B': 'b'}, A='a', B='b')
