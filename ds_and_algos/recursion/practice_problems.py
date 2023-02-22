from functools import reduce

# def binary_strings(n):
#     # if n == 0: 
#     #     print(slate)
#     #     return
#     # # add "0"
#     # binary_strings(n-1, slate+"0")
#     # # add "1"
#     # binary_strings(n-1, slate+"1")

#     result = []
#     def helper(n, slate=""):
#         if n == 0:
#             result.append(slate)
#             return
#         # add 0
#         helper(n-1, slate+"0")
#         # add 1
#         helper(n-1, slate+"1")
#     helper(n)
#     return result

# # r = binary_strings(n=3)
# # print('binary strings', r)

# # 784
# def letter_case_permutations(S):
#     result = []
#     def helper(slate, S):
#         # base case
#         if len(S) == 0: 
#             result.append(slate)
#             return
#         if S[0].isnumeric():
#             helper(slate + S[0], S[1:])
#         else:
#             helper(slate + S[0], S[1:])
#             helper(slate+S[0].upper(), S[1:])
#     helper("", S)
#     return result

# # print('letter case permutations', letter_case_permutations(S='1122'))

# # 78
# def subsets(nums):
#     result = []
#     def helper(nums, slate):
#         # base case 
#         if len(nums) == 0:
#             result.append(slate[:])
#             return
#         # exclude
#         helper(nums[1:], slate)
#         # include
#         slate.append(nums[0])
#         helper(nums[1:], slate)
#         slate.pop()
#         return
#     helper(nums, [])
#     return result

# print('subsets:', subsets([1,2,3]))

# # 46
# def permutations(arr):
#     result = []
#     def helper(arr, slate=[]):
#         # base case
#         if len(arr) == 0:
#             result.append(slate[:])
#             return
#         for i in range(len(arr)):
#             slate.append(arr[i])
#             helper(arr[:i]+arr[i+1:], slate)
#             slate.pop()
#     helper(arr)
#     return result

# # print('permutations:', permutations([1,2,3]))

# # 47: given a collection of numbers that might contain duplicates return all possible unique permutations
# # input: [1,1,2]
# # output: [1,1,2], [1,2,1], [2,1,1]
# def permutations_unqiue(arr):
#     result = []
#     def helper(arr, slate=[]):
#         # base
#         if len(arr) == 0:
#             result.append(slate[:])
#             return
#         d = dict()
#         for i in range(len(arr)):
#             if arr[i] in d:
#                 continue
#             d[arr[i]] = 1
#             slate.append(arr[i])
#             helper(arr[:i]+arr[i+1:], slate)
#             slate.pop()
#     helper(arr)
#     return result

# # print('permutations unique:', permutations_unqiue([1,1,2]))

# def subsets_alternative(nums):
#     result = []
#     def helper(slate, nums):
#         result.append(slate[:])
#         # base case 
#         if len(nums) == 0:
#             return
#         for i in range(len(nums)):
#             slate.append(nums[i])
#             helper(slate, nums[i+1:])
#             slate.pop()
#     helper([], nums)
#     return result

# # print('subsets alternative:', subsets_alternative([1,2,3]))

#90
def subsets_unique(nums):
    result = []
    nums.sort()
    def helper(slate, nums):
        result.append(slate[:])
        # base case 
        if len(nums) == 0:
            return
        prev_num = None
        for i in range(len(nums)):
            if prev_num == nums[i]:
                continue
            slate.append(nums[i])
            helper(slate, nums[i+1:])
            slate.pop()
            prev_num = nums[i]
    helper([], nums)
    return result

print('subsets unique:', subsets_unique([1,2,2,3]))

# # 17. Letter combination on phone #
# def phone_number(nums):
#     letter_mapping = {
#         2: ['a', 'b','c'],
#         3: ['d', 'e', 'f'],
#         4: ['g', 'h', 'i'],
#         # ...
#     }
#     result = []
#     def helper(slate, nums):
#         # base case
#         if len(nums) == 0:
#             result.append(slate[:])
#             return
#         for i in range(len(letter_mapping[nums[0]])):
#             slate.append(letter_mapping[nums[0]][i])
#             helper(slate, nums[1:])
#             slate.pop()
#     helper([], nums)
#     return result

# # print('phone number:', phone_number([2,3]))

# # 77 Combinations 
# def C(n,k):
#     result = []
#     def helper(nums, k, slate=[]):
#         # backtrack case
#         if len(slate) == k:
#             result.append(slate[:])
#             return
#         # base case
#         if len(nums) == 0:
#             return
#         # recursive case
#         for i in range(len(nums)):
#             slate.append(nums[i])
#             helper(nums[i+1:], k, slate)
#             slate.pop()
#     helper(list(range(1,n+1)), k)
#     return result

# print('C(n,k):', C(4,2))

# def parentheses(n):
#     result = []
#     def helper(n, L_count=0, R_count=0, slate=[]):
#         # backtrack case
#         if R_count > L_count or L_count > 3:
#             return
#         # result case
#         if L_count == R_count == 3:
#             result.append(slate[:])
#             return
#         # add left parenthese
#         slate.append('(')
#         helper(n, L_count+1, R_count, slate)
#         slate.pop()
#         # add right parenthese
#         slate.append(')')
#         helper(n, L_count, R_count+1, slate)
#         slate.pop()
#     helper(n)
#     return [reduce(lambda x, y: x+y, r) for r in result]

# # print('Generate parentheses:', parentheses(3))