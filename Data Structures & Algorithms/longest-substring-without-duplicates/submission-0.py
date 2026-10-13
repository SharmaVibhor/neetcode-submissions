class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        result = 0
        leftIndex = 0

        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[leftIndex])
                leftIndex += 1
            charSet.add(s[i])

            result = max(result, i - leftIndex +1)

        return result
        