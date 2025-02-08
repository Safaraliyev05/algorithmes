# class Solution:
#     def missingNumber(self, nums):
#         maximum = max(nums)
#         for i in range(maximum):
#             nums.sort()
#

def problem(num):
    count = 0
    for i in range(1, num + 1):
        count += i
        return count

if __name__ == '__main__':
    print(problem(5))