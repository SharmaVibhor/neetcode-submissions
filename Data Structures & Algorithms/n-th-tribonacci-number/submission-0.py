class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {0:0,1:1,2:1}

        for n in range(3,n+1):
            dp[n] = dp[n-1] + dp[n-2] + dp[n-3]

        return dp[n]
        