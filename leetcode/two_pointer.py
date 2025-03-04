# Two pointer
# nums = [4, 2, 1, 5, 8, 3, 6, 7]
# nums.sort()
#
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == 8:
#             print(nums[i], nums[j])
#
#
# def two_pointer(nums, target):
#     nums.sort()
#     left, right = 0, len(nums) - 1
#     while left <= right:
#         if nums[left] + nums[right] == target:
#             return True
#         elif nums[left] + nums[right] < target:
#             left += 1
#         else:
#             right -= 1
#     return False


# def maxArea(nums: list) -> int:
#     left, right = 0, len(nums) - 1
#     max_area = 0
#     while left <= right:
#         area = (right - left) * min(nums[left], nums[right])
#         max_area = max(max_area, area)
#         if nums[left] < nums[right]:
#             left += 1
#         else:
#             right -= 1
#     return max_area

# print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

# prefix precompute
# def sign(num):
#     if num < 0:
#         return -1
#     elif num > 0:
#         return 1
#     return 0
#
#
# def leftRightDifference(nums: list) -> list:
#     left, right = 0, sum(nums)
#     result = []
#
#     for num in nums:
#         right -= num
#         result.append(sign(right - left))
#         left += num
#     return result
#
#
# def productExceptSelf(nums: list) -> list:
#     prefix = [1]
#     suffix = [1]
#
#     product = 1
#     for num in nums:
#         product *= num
#         prefix.append(product)
#
#     product = 1
#     for num in reversed(nums):
#         product *= num
#         suffix.append(product)
#     suffix.reverse()
#
#     result = []
#     for i in range(len(nums)):
#         left, right = 1, 1
#         left = prefix[i]
#         right = suffix[i + 1]
#         prod = left * right
#         result.append(prod)
#
#     return result


# string tasks
# 1
# s = ["h", "e", "l", "l", "o"]
#
#
# def reverseString(s: list) -> list:
#     left, right = 0, len(s) - 1
#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left += 1
#         right -= 1
#     return s
#
#
# print(reverseString(s))

# 2
# OPEN = '('
# CLOSE = ')'
#
#
# def is_valid(s: str) -> bool:
#     balance = 0
#     for bracket in s:
#         if bracket == OPEN:
#             balance += 1
#         elif bracket == CLOSE:
#             balance -= 1
#
#         if balance < 0:
#             return False
#
#     return balance == 0

# 3
# def detectCapitalUse(word: str) -> bool:
#     return word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower())
#
#
# print(detectCapitalUse("USA"))
# print(detectCapitalUse("FlaG"))

# 4
# def longestCommonPrefix(words: list) -> str:
#     short = min(words, key=len)
#     m = len(short)
#     prefix = ""
#
#     for i in range(m):
#         for word in words:
#             if short[i] != word[i]:
#                 return prefix
#         prefix = short[:i + 1]
#
#     return prefix
#
#
# print(longestCommonPrefix(["flower", "flow", "flight"]))
