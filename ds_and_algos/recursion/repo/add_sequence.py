

def add_sequence(n, b1, b2):
    print('n:', n, 'b1:', b1, 'b2:', b2)
    if n==0:
        print('returning', b1)
        return b1
    # if n==1:
    #     return b2
    else:
        return add_sequence(n-1, b2, b1+b2)

# r = add_sequence(5, 2, 4)
# print(r)

# x = 3
# for i in range(1,5):
#     x *= i
#     print(x)

# print(x)


def fib(n, b1, b2):
    if n == 0: return b1
    return fib(n-1, b1=b2, b2=b1+b2)

r = fib(6, 0, 1)
print(r)