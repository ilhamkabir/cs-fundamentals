# generators

# -------- without generator ----------

# def square_nums(nums):
#     result = []
#     for num in nums:
#         result.append(num*num)
#     return result

# my_nums = square_nums([1, 2, 3, 4, 5])
# print(my_nums)

# # list comprehension
# my_nums = [x*x for x in [1, 2, 3, 4, 5]]
# print(my_nums)

# -------- with generator ----------

# def square_nums(nums):
#     for i in nums:
#         yield(i*i)

# my_nums = square_nums([1, 2, 3, 4, 5])

# # for num in my_nums:
# #     print(num)

# print('1:',  next(my_nums))
# print('2:',  next(my_nums))
# print('3:',  next(my_nums))
# print('4:',  next(my_nums))
# print('5:',  next(my_nums))
# print('6:',  next(my_nums)) # StopIterator exception

# generator comprehension
my_nums = (x*x for x in [1, 2, 3, 4, 5]) # <- () not []
print(next(my_nums))
print(next(my_nums))

# ------------------


