# class Solution:
#     def missingNumber(self, nums):
#         maximum = max(nums)
#         for i in range(maximum):
#             nums.sort()
#

# def print_full_name(first, last):
#     print(f"Hello {first} {last}! You just delved into python.")
#
#
# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)

# def mutate_string(string, position, character):
#     l = list(string)
#     l[position] = character
#     string = ''.join(l)
#     return string
#
#
# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)

# Array 2011
# class Solution:
#     def finalValueAfterOperations(self, operations: List[str]) -> int:
#         count = 0
#         for i in operations:
#             if i[1] == "+":
#                 count += 1
#             else:
#                 count -= 1
#         return count

# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         return nums + nums

# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         count = 0
#         for num in nums:
#             if num == nums[0]:
#                 count += 1
#         return count
#
#
# hi = Solution()
# print(hi.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
