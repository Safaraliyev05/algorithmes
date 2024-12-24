# # 507 Perfect Number
# class Solution(object):
#     def checkPerfectNumber(self, num):
#         count = 0
#         for i in range(1, num):
#             if num % i == 0:
#                 count += i
#
#         if count == num:
#             return True
#         return False
#
#
# hi = Solution()
# print(hi.checkPerfectNumber(28))

# 728. Self Dividing Numbers
# class Solution:
#     def selfDividingNumbers(self, left: int, right: int):
#         def func(num):
#             for digit in str(num):
#                 if digit == '0' or num % int(digit) != 0:
#                     return False
#             return True
#
#         nums = []
#         for i in range(left, right + 1):
#             if func(i):
#                 nums.append(i)
#
#         return nums
#
#
# hi = Solution()
# print(hi.selfDividingNumbers(1, 22))
