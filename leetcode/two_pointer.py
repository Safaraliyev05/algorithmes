# Two pointer
nums = [4, 2, 1, 5, 8, 3, 6, 7]
nums.sort()

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == 8:
            print(nums[i], nums[j])


def two_pointer(nums, target):
    nums.sort()
    left, right = 0, len(nums) - 1
    while left <= right:
        if nums[left] + nums[right] == target:
            return True
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
    return False
