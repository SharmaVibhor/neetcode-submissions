class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n ==0:
            return 1

        res = x
        for i in range(1,abs(n)):
            res = res*x
        
        if n<0:
            res = 1/res

        return res
        