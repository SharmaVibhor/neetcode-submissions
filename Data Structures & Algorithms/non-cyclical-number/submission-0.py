class Solution:
    def helper(self, n: int) -> int:
        res = 0
        while(n):
            digit = n%10
            res+= digit*digit
            n = n//10
        return res

    def isHappy(self, n: int) -> bool:
        results = set()

        while(n not in results):
            results.add(n)
            n = self.helper(n)
            if n==1:
                return True
        
        return False

        