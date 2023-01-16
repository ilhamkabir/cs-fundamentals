

# def binary_strings(n):
#     print('n', n)
#     if n == 1:
#         return ["0", "1"]
#     else:
#         prev = binary_strings(n-1)
#         print('prev:', prev)
#         result = []
#         for s in prev:
#             print('s', s)
#             result.append(s + "0")
#             result.append(s + "1")
#         print('result:', result)
#         return result

# def binary_strings(n):
#     result = ["0", "1"]
#     for iter in range(2, n+1):
#         new_result = []
#         for s in result:
#             new_result.append(s+"0")
#             new_result.append(s+"1")
#         result = new_result
#     return result

def helper(slate, n):
    print(n, slate)
    if n == 0:
        print(slate)
    else:
        helper(slate+"0", n-1)
        helper(slate+"1", n-1)

def binary_strings(n):
    helper("", n)

r = binary_strings(3)
print('answer:', r)  