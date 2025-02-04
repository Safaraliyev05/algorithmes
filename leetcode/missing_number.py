# class Solution:
#     def missingNumber(self, nums):
#         maximum = max(nums)
#         for i in range(maximum):
#             nums.sort()
#

class Solution:
    def singleNumber(self, nums):
        for i in nums:
            if nums.count(i) == 1:
                return i


hi = Solution()
print(hi.singleNumber([2, 2, 1, 1, 3, 3]))
