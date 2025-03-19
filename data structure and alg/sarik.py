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

# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#
#
# hi = Solution()
# hi.moveZeroes([0, 1, 0, 3, 12])

def func(n):
    if n < 1:
        print("1 dan kop")
        return

    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                print("X")
            else:
                print(" ")
        print()


size = int(input("Enter: "))
func(size)
