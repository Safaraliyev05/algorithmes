# 1
def reverseString(s: list) -> list:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


# 2
OPEN = '('
CLOSE = ')'


def is_valid(s: str) -> bool:
    balance = 0
    for bracket in s:
        if bracket == OPEN:
            balance += 1
        elif bracket == CLOSE:
            balance -= 1

        if balance < 0:
            return False

    return balance == 0


# 3
def detectCapitalUse(word: str) -> bool:
    if word == word.capitalize():
        return True
    elif word == word.upper():
        return True
    elif word == word.lower():
        return True
    else:
        return False


# 4
def longestCommonPrefix(words: list) -> str:
    short = min(words, key=len)
    m = len(short)
    prefix = ""

    for i in range(m):
        for word in words:
            if short[i] != word[i]:
                return prefix
        prefix = short[:i + 1]

    return prefix


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
