# 1
def moveZeroes(nums: list) -> list:
    count = 0
    for i, num in enumerate(nums):
        if num == 0:
            count += 1
            continue
        nums[i], nums[i - count] = nums[i - count], nums[i]

    return nums


moveZeroes([0, 1, 0, 3, 12])


# 2 Two Pointer
def reverse(nums, i, j):
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1


def rotate(nums: list, k: int) -> list:
    k = k % len(nums)
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)
    return nums


print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(rotate([-1, -100, 3, 99], 2))


# 3 Pascal triangle
def generate_row(prev):
    next_ = [1]
    for i in range(len(prev) - 1):
        next_.append(prev[i] + prev[i + 1])
    next_.append(1)
    return next_


def generate(n: int) -> list:
    if n == 0:
        return []

    row = [1]
    result = [row]

    for i in range(n - 1):
        row = generate_row(row)
        result.append(row)

    return result


print(generate(2))
print(generate(5))


# 4 Two pointer
def sortedSquares(nums: list) -> list:
    i, j = 0, len(nums) - 1
    result = []

    while i <= j:
        if abs(nums[i]) < abs(nums[j]):
            result.append(nums[j] ** 2)
            j -= 1
        else:
            result.append(nums[i] ** 2)
            i += 1

    result.reverse()
    return result


# 5 Two pointer
def maxArea(nums: list) -> int:
    left, right = 0, len(nums) - 1
    max_area = 0
    while left <= right:
        area = (right - left) * min(nums[left], nums[right])
        max_area = max(max_area, area)
        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1
    return max_area


# 6 prefix precompute
def sign(num):
    if num < 0:
        return -1
    elif num > 0:
        return 1
    return 0


def leftRightDifference(nums: list) -> list:
    left, right = 0, sum(nums)
    result = []

    for num in nums:
        right -= num
        result.append(sign(right - left))
        left += num
    return result


# 7 Prefix/Suffix
def productExceptSelf(nums: list) -> list:
    prefix = [1]
    suffix = [1]

    product = 1
    for num in nums:
        product *= num
        prefix.append(product)

    product = 1
    for num in reversed(nums):
        product *= num
        suffix.append(product)
    suffix.reverse()

    result = []
    for i in range(len(nums)):
        left, right = 1, 1
        left = prefix[i]
        right = suffix[i + 1]
        prod = left * right
        result.append(prod)

    return result
