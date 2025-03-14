# def moveZeroes(nums: list) -> list:
#     count = 0
#     for i, num in enumerate(nums):
#         if num == 0:
#             count += 1
#             continue
#         nums[i], nums[i - count] = nums[i - count], nums[i]
#     return nums
#
#
# print(moveZeroes([0, 1, 0, 3, 12]))
from typing import List


# 2
# def reverse(nums, i, j):
#     while i < j:
#         nums[i], nums[j] = nums[j], nums[i]
#         i += 1
#         j -= 1
#
#
# def rotate(nums: list, k: int) -> list:
#     k = k % len(nums)
#     reverse(nums, 0, len(nums) - 1)
#     reverse(nums, 0, k-1)
#     reverse(nums, k, len(nums) - 1)
#     return nums
#
#
# print(rotate([1, 2, 3, 4, 5, 6, 7], 3))

# 3 Pascal`s triangle
# def generate_row(prev):
#     next_ = [1]
#     for i in range(len(prev) - 1):
#         next_.append(prev[i] + prev[i + 1])
#     next_.append(1)
#     return next_
#
#
# def generate(n: int) -> list:
#     if n == 0:
#         return []
#
#     row = [1]
#     result = [row]
#
#     for i in range(n):
#         row = generate_row(row)
#         result.append(row)
#
#     return result[-1]
#
#
# print(generate(3))

# class Solution:
#     def generate_row(self, prev):
#         next_ = [1]
#         for i in range(len(prev) - 1):
#             next_.append(prev[i] + prev[i + 1])
#         next_.append(1)
#         return next_
#
#     def getRow(self, rowIndex: int) -> List[int]:
#         if rowIndex == 0:
#             return [1]
#
#         row = [1]
#         result = [row]
#
#         for i in range(rowIndex):
#             row = self.generate_row(row)
#             result.append(row)
#
#         return result[-1]
#
#
# hi = Solution()
# print(hi.getRow(3))


# Two pointer
# nums = [4, 2, 1, 5, 8, 3, 6, 7]
# nums.sort()

# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == 8:
#             print(nums[i], nums[j])

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
#
#
# def three_sum(nums, target=0):
#     nums.sort()
#     result = []
#
#     for i in range(len(nums) - 2):
#         left, right = i + 1, len(nums) - 1
#
#         while left < right:
#             if nums[i] + nums[left] + nums[right] == target:
#                 result.append([nums[i], nums[left], nums[right]])
#                 left += 1
#                 right -= 1
#             elif nums[i] + nums[left] + nums[right] < target:
#                 left += 1
#             else:
#                 right -= 1
#
#     return result
#
#
# def middle(nums, target):
#     nums.sort()  # O(N, log(N))
#     for i in range(len(nums) - 1):  # O(n)
#         left, right = i + 1, len(nums) - 1
#         while left < right:  # O(log(N))
#             mid = (left + right) // 2
#             if nums[i] + nums[mid] == target:
#                 return True
#             elif nums[i] + nums[mid] > target:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return False


# print(two_pointer([1, 3, 5, 7, 9, 11, 14], 16))
# print(three_sum([1, 3, 5, 7, 9, 11, 14], 17))
# print(middle([1, 3, 5, 7, 9, 11, 14], 20))

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """


hi = Solution()
hi.moveZeroes([0, 1, 0, 3, 12])
