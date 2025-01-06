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

# 13. Roman to Integer
# class Solution:
#     def romanToInt(self, s):
#
#         roman_to_int = {
#             'I': 1, 'V': 5, 'X': 10, 'L': 50,
#             'C': 100, 'D': 500, 'M': 1000
#         }
#
#         result = 0
#
#         for i in range(len(s)):
#             if i < len(s) - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
#                 result -= roman_to_int[s[i]]
#             else:
#                 result += roman_to_int[s[i]]
#
#         return result

# class Solution:
#     def plusOne(self, digits):
#         number = int(''.join(map(str, digits)))
#         add_one = number + 1
#         result = [int(digit) for digit in str(add_one)]
#         return result
#
#
# hi = Solution()
# print(hi.plusOne([1, 2, 3, 4]))

# class Solution(object):
#     def mySqrt(self, x):
#         return int(sqrt(x))

# class Solution(object):
#
#     def addDigits(self, num):
#         if num < 10:
#             return num
#         return self.addDigits(sum(int(digit) for digit in str(num)))


# class Solution(object):
#     def addStrings(self, num1, num2):
#         return str(int(num1) + int(num2))

# 1903 Not solved
# class Solution(object):
#     def largestOddNumber(self, num: str):
#         max_odd = -1
#         if int(num) % 2 == 1:
#             return num
#         else:
#             for i in num:
#                 if int(i) % 2 == 1:
#                     return str(max(max_odd, int(i)))
#             return ''
