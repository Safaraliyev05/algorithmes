# 268
# class Solution:
#     def missingNumber(self, nums):
#         nums.sort()
#         for i in range(len(nums)):
#             if i != nums[i]:
#                 return i
#
#
# hi = Solution()
# print(hi.missingNumber([3, 0, 1]))
#
# def print_full_name(first, last):
#     print(f"Hello {first} {last}! You just delved into python.")
#
#
# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)
#
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
#
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
#
# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         return nums + nums
#
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
#
#
# 217
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] == nums[j]:
#                     return True
#         return False
#
#
# hi = Solution()
# print(hi.containsDuplicate([1, 2, 3, 4]))


# 977
# class Solution(object):
#     def sortedSquares(self, nums):
#         i, j = 0, len(nums) - 1
#         result = []
#
#         while i <= j:
#             if abs(nums[i]) < abs(nums[j]):
#                 result.append(nums[j] ** 2)
#                 j -= 1
#             else:
#                 result.append(nums[i] ** 2)
#                 i += 1
#         result.reverse()
#         return result
#
#
# hi = Solution()
# print(hi.sortedSquares([-4, -1, 0, 3, 10]))

# 961
# class Solution(object):
#     def repeatedNTimes(self, nums):
#         n = len(nums) // 2
#         for i in nums:
#             if nums.count(i) == n:
#                 return i
#
# hi = Solution()
# print(hi.repeatedNTimes([1, 2, 3, 3]))
# print(hi.repeatedNTimes([2, 1, 2, 5, 3, 2]))
# print(hi.repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]))
#
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(len(nums)):
#     print(i, nums[i])

# 922
# class Solution(object):
#     def sortArrayByParityII(self, nums):
#         even_index = 0
#         odd_index = 1
#         n = len(nums)
#
#         while even_index < n and odd_index < n:
#             if nums[even_index] % 2 == 0:
#                 even_index += 2
#             elif nums[odd_index] % 2 == 1:
#                 odd_index += 2
#             else:
#                 nums[even_index], nums[odd_index] = nums[odd_index], nums[even_index]
#                 even_index += 2
#                 odd_index += 2
#
#         return nums
#
# hi = Solution()
# print(hi.sortArrayByParityII([4, 1, 2, 1]))

# 905
# class Solution(object):
#     def sortArrayByParity(self, nums):
#         i, j = 0, len(nums) - 1
#         while i < j:
#             if nums[i] % 2 == 0:
#                 i += 1
#             else:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 j -= 1
#         return nums
#
#
# hi = Solution()
# print(hi.sortArrayByParity([3, 1, 2, 4]))

# 1967
# class Solution(object):
#     def numOfStrings(self, patterns, word):
#         count = 0
#         for i in patterns:
#             if i in word:
#                 count += 1
#         return count
#
#
# hi = Solution()
# print(hi.numOfStrings(["a", "abc", "bc", "d"], "abc"))
# print(hi.numOfStrings(["a", "b", "c"], "aaaaabbbbb"))

# 3190
# class Solution(object):
#     def minimumOperations(self, nums):
#         count = 0
#         for i in nums:
#             if i % 3 != 0:
#                 count += 1
#         return count
#
#
# hi = Solution()
# print(hi.minimumOperations([1, 2, 3, 4]))
# print(hi.minimumOperations([3, 6, 9]))

# 2942
# class Solution(object):
#     def findWordsContaining(self, words, x):
#         result = []
#         count = 0
#         for word in words:
#             if x in word:
#                 result.append(count)
#             count += 1
#         return result
#
#
# hi = Solution()
# print(hi.findWordsContaining(["leet", "code"], 'e'))
# print(hi.findWordsContaining(["abc", "bcd", "aaaa", "cbc"], 'a'))
# print(hi.findWordsContaining(["abc", "bcd", "aaaa", "cbc"], 'z'))

# 3452 ----------------
# class Solution(object):
#     def sumOfGoodNumbers(self, nums, k):
#         count = 0
#         for i, num in enumerate(nums):
#             print(i, num)
#             if i - k > num and i + k > num:
#                 count += num
#         return count
#
#
# hi = Solution()
# print(hi.sumOfGoodNumbers([1, 3, 2, 1, 5, 4], 2))
#
# def create_matrix(n):
#     matrix = []
#     for i in range(n):
#         row = []
#         for j in range(n):
#             if i == j:
#                 row.append(0)
#             else:
#                 row.append(1)
#         matrix.append(row)
#     return matrix
#
#
# matrix = (create_matrix(4))
# for row in matrix:
#     print(row)


# 682
# class Solution(object):
#     def calPoints(self, operations):
#         record = []
#         for nums in operations:
#             if nums == "C":
#                 record.pop()
#             elif nums == "D":
#                 record.append(2 * record[-1])
#             elif nums == "+":
#                 record.append(record[-1] + record[-2])
#             else:
#                 record.append(int(nums))
#         return sum(record)
#
#
# hi = Solution()
# print(hi.calPoints(["5", "2", "C", "D", "+"]))

# Sliding window
# def func(nums, k):
#     sum = 0
#     maximum = sum
#     for i in range(k):
#         sum += nums[i]
#
#     for i in range(k, len(nums)):
#         sum += nums[i]
#         sum -= nums[i - k]
#         if maximum < sum:
#             maximum = sum
#
#     return maximum
#
#
# print(func([4, 8, 3, 0, 5, 6, 9, 1], 4))

# class Solution(object):
#     def decrypt(self, code, k):
#         answer = [0] * len(code)
#
#         if k == 0:
#             return [0] * len(code)
#
#         for i in range(len(code)):
#             count = 0
#             if k > 0:
#                 for j in range(1, k + 1):
#                     count += code[(i + j) % len(code)] # 3, 2, 1.
#             else:
#                 for j in range(1, -k + 1):
#                     count += code[(i - j) % len(code)]
#             answer[i] = count
#
#         return answer
#
#
# hi = Solution()
# print(hi.decrypt([5, 7, 1, 4], 3))
# print(hi.decrypt([1, 2, 3, 4], 0))
# print(hi.decrypt([2, 4, 9, 3], -2))

# 58
# class Solution(object):
#     def lengthOfLastWord(self, s):
#         return len((s.split())[-1])
#
#
# hi = Solution()
# print(hi.lengthOfLastWord("hello world"))
# print(hi.lengthOfLastWord("   fly me   to   the moon  "))
# print(hi.lengthOfLastWord("luffy is still joyboy"))

# 3289
# class Solution(object):
#     def getSneakyNumbers(self, nums):
#         result = []
#         my_set = set()
#         for num in nums:
#             if num not in my_set:
#                 my_set.add(num)
#             else:
#                 result.append(num)
#         return result
#
#
# hi = Solution()
# print(hi.getSneakyNumbers([0, 3, 2, 1, 3, 2]))
# print(hi.getSneakyNumbers([0, 1, 1, 0]))
#
#
# # 771
# class Solution(object):
#     def numJewelsInStones(self, jewels, stones):
#         result = 0
#         for stone in stones:
#             if stone in jewels:
#                 result += 1
#         return result
#
#
# hi = Solution()
# print(hi.numJewelsInStones(jewels="aA", stones="aAAbbbb"))
# print(hi.numJewelsInStones(jewels="z", stones="ZZ"))


# 1684
# class Solution(object):
#     def countConsistentStrings(self, allowed, words):
#         words = set(words)
#         result = 0
#
#
# hi = Solution()
# print(hi.countConsistentStrings(allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"]))

# 1920
# class Solution(object):
#     def buildArray(self, nums):
#         result = []
#         for i in range(len(nums)):
#             result.append(nums[nums[i]])
#         return result
#
#
# hi = Solution()
# print(hi.buildArray([0, 2, 1, 5, 3, 4])) # [0,1,2,4,5,3]
# print(hi.buildArray([5, 0, 1, 2, 3, 4])) # [4,5,0,1,2,3]

# 1512
# class Solution(object):
#     def numIdenticalPairs(self, nums):
#         count = 0
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] == nums[j]:
#                     count += 1
#         return count
# 
# 
# hi = Solution()
# print(hi.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
# print(hi.numIdenticalPairs([1, 1, 1, 1]))
# print(hi.numIdenticalPairs([1, 2, 3]))

# 1290
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def getDecimalValue(self, head):
#         stringbuilder = ''
#         current = head
#
#         while current != None:
#             stringbuilder += str(current.val)
#             current = current.next
#
#         return int(stringbuilder, 2)

# 3467
# class Solution(object):
#     def transformArray(self, nums):
#         result = []
#         for i in nums:
#             if i % 2 == 0:
#                 result.append(0)
#             else:
#                 result.append(1)
#
#         return sorted(result)

# 1672
# class Solution(object):
#     def maximumWealth(self, accounts):
#         maximum = 0
#         for account in accounts:
#             if maximum < sum(account):
#                 maximum = sum(account)
#         return maximum
#
#
# hi = Solution()
# print(hi.maximumWealth([[1, 2, 3], [3, 2, 1]]))
# print(hi.maximumWealth([[1, 5], [7, 3], [3, 5]]))
# print(hi.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))

# 1431
# class Solution(object):
#     def kidsWithCandies(self, candies, extraCandies):
#         result = []
#         maximum = max(candies)
#         for candy in candies:
#             if candy + extraCandies >= maximum:
#                 result.append(True)
#             else:
#                 result.append(False)
#         return result
#
#
# hi = Solution()
# print(hi.kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3))
# print(hi.kidsWithCandies([4, 2, 1, 1, 2], extraCandies=1))
# print(hi.kidsWithCandies(candies=[12, 1, 12], extraCandies=10))

# 1470
# class Solution(object):
#     def shuffle(self, nums, n):
#         result = []
#         for i in range(n):
#             result.append(nums[i])
#             result.append(nums[i + n])
#         return result
#
# hi = Solution()
# print(hi.shuffle(nums=[2, 5, 1, 3, 4, 7], n=3))

# 3162
# class Solution(object):
#     def numberOfPairs(self, nums1, nums2, k):
#         count = 0
#         for i in nums1:
#             for j in nums2:
#                 if i % (j * k) == 0:
#                     count += 1
#         return count
#
#
# hi = Solution()
# print(hi.numberOfPairs(nums1=[1, 3, 4], nums2=[1, 3, 4], k=1))

# 1816
# class Solution(object):
#     def truncateSentence(self, s, k):
#         return ' '.join(s.split()[:k])
#
#
# hi = Solution()
# print(hi.truncateSentence(s="Hello how are you Contestant", k=4))

# 1662
# class Solution(object):
#     def arrayStringsAreEqual(self, word1, word2):
#         r1 = ''.join(word1)
#         r2 = ''.join(word2)
#         return r1 == r2
#
#
# hi = Solution()
# print(hi.arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"]))
# print(hi.arrayStringsAreEqual(["a", "cb"], word2=["ab", "c"]))
# print(hi.arrayStringsAreEqual(["abc", "d", "defg"], word2=["abcddefg"]))

# 2000
# class Solution(object):
#     def reversePrefix(self, word, ch):
#         for index, w in enumerate(word):
#             if w == ch:
#                 return word[:index + 1][::-1] + word[index + 1:]
#         return word
#
#
# hi = Solution()
# print(hi.reversePrefix(word="abcdefd", ch="d")) # dcbaefd
# print(hi.reversePrefix(word="xyxzxe", ch="z")) # zxyxxe
# print(hi.reversePrefix(word="abcd", ch="z")) # abcd

# 3194
# class Solution(object):
#     def minimumAverage(self, nums):
#         nums.sort()
#         result = []
#         left, right = 0, len(nums) - 1
#
#         while left < right:
#             avg = round((nums[left] + nums[right]) / 2.0, 1)
#             result.append(avg)
#             left += 1
#             right -= 1
#
#         return min(result)
#
#
# hi = Solution()
# print(hi.minimumAverage([7, 8, 3, 4, 15, 13, 4, 1]))

# 2418
# class Solution(object):
#     def sortPeople(self, names, heights):
#         sorted_people = sorted(zip(heights, names), reverse=True)
#         return [name for _, name in sorted_people]
#
#
# hi = Solution()
# print(hi.sortPeople(names=["Mary", "John", "Emma"], heights=[180, 165, 170]))

# 1684 --------------
# class Solution(object):
#     def countConsistentStrings(self, allowed, words):
#         count = 0
#         for word in words:
#             if set(word).issubset(allowed):
#                 count += 1
#         return count
#
#
# hi = Solution()
# print(hi.countConsistentStrings(allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"]))  # 2
# print(hi.countConsistentStrings(allowed="abc", words=["a", "b", "c", "ab", "ac", "bc", "abc"]))  # 7

# 1 -------------- hash map
# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#
#
# hi = Solution()
# print(hi.twoSum(nums=[2, 7, 11, 15], target=9))
# print(hi.twoSum(nums=[3, 2, 4], target=6))
# print(hi.twoSum(nums=[3, 3], target=6))
# print(hi.twoSum(nums=[2, 5, 5, 11], target=10))

# 2
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        curr1, curr2 = l1, l2
        head = curr = ListNode(0)
        while curr1 or curr2:
            total = sum([
                curr1.val if curr1 else 0,
                curr2.val if curr2 else 0,
                carry,
            ])

            digit = total % 10
            carry = total // 10
            curr.next = ListNode(digit)
            curr = curr.next
            if curr1: curr1 = curr1.next
            if curr2: curr2 = curr2.next

        if carry:
            curr.next = ListNode(carry)

        return head.next
