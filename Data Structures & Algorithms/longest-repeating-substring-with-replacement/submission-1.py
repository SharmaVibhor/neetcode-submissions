class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        leftIndex = 0

        for rightIndex in range(len(s)):
            count[s[rightIndex]] = 1 + count.get(s[rightIndex],0)

            if (rightIndex-leftIndex + 1) - max(count.values()) > k :
                count[s[leftIndex]] -= 1
                leftIndex += 1

            result = max(result, rightIndex-leftIndex + 1)

        return result
        