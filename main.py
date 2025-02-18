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

# 3
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
#     for i in range(n - 1):
#         row = generate_row(row)
#         result.append(row)
#
#     return result
#
# print(generate(4))

