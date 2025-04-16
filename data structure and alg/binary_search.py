# sorted array, TIME: O(Log(n) + Log(n)) = O(N Log(N))
# l = [1, 9, 3, 0, 7, 8, 14]  # TIME = O(n) linear search
# l.sort()  # TIME = O(N Log(n))
# left, right = 0, len(l) - 1
#
# target = 14
# while left <= right:  # TIME O(Log(n))
#     mid = (left + right) // 2
#     if l[mid] == target:
#         # print(target)
#         break
#     elif l[mid] > target:
#         right = mid - 1
#     else:
#         left = mid + 1
# else:
#     # print("Target not found")
#     pass


# 2824
# class Solution(object):
#     def countPairs(self, nums, target):
#         if len(nums) < 2:
#             return 0
#         count = 0
#         nums.sort()
#         left, right = 0, len(nums) - 1
#         # for i in range(len(nums)):
#         #     for j in range(i + 1, len(nums)):
#         #         if nums[i] + nums[j] < target:
#         #             count += 1
#         # return count
#         while left <= right:
#             s = nums[left] + nums[right]
#             if s < target:
#                 count += (right - left)
#                 left += 1
#             else:
#                 right -= 1
#         return count
#
#
# hi = Solution()
# print(hi.countPairs(nums=[-1, 1, 2, 3, 1], target=2))

# 2089
# class Solution(object):
#     def targetIndices(self, nums, target):
#         nums.sort()
#         result = []
#         # for i, num in enumerate(nums):
#         #     if num == target:
#         #         result.append(i)
#         # return result
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#
#         while left < len(nums) and nums[left] == target:
#             result.append(left)
#             left += 1
#
#         return result
#
#
# hi = Solution()
# print(hi.targetIndices(nums=[1, 2, 5, 2, 3], target=2))
# print(hi.targetIndices(nums=[1, 2, 5, 2, 3], target=3))
# print(hi.targetIndices(nums=[1, 2, 5, 2, 3], target=5))
#
#
# # 349
# class Solution(object):
#     def intersection(self, nums1, nums2):
#         result = []
#         return list(set(nums1) & set(nums2))
#
#
# hi = Solution()
# print(hi.intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]))

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def search(root, key):
    if root is None:
        return False
    if root.val == key:
        return True
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


root = None
root = insert(root, 50)
insert(root, 25)
insert(root, 70)

if search(root, 25):
    print("Found")
else:
    print("Not Found")
