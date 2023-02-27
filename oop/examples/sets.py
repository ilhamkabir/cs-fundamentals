x = {1, 2, 3}
y = set([1,2,3])

print(x == y) # True
print(x is y) # False

x.add(4)
x.update([5,6,7])
x.remove(1)

print(x) # {2, 3, 4, 5, 6, 7}

print(x.difference(y)) # {4, 5, 6, 7}
print(x.symmetric_difference(y)) # {1, 4, 5, 6, 7}

print(x.union(y)) # {1, 2, 3, 4, 5, 6, 7}
print(x.intersection(y)) # {2, 3}
