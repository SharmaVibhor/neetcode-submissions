class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ""

        def helper(a,b):
            return a if b == 0 else helper(b, a % b)

        g = helper(len(str1), len(str2))
        return str1[:g]
        

        