class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            if n==1:
                return x

            if n%2 == 0:
                temp = helper(x,n/2)
                return temp*temp
            else:
                temp = helper(x,(n-1)/2)
                return temp*temp*x


        res = helper(x,abs(n))
        return res if n>=0 else 1 / res
        