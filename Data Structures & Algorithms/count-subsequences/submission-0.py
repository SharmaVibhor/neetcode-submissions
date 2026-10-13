class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]
        
        for i in range(len(s)+1):
            dp[len(t)][i]=1

        for r in range(len(t)-1,-1,-1):
            for c in range(len(s)-1,-1,-1):
                dp[r][c]=dp[r][c+1]
                if t[r] == s[c]:
                    dp[r][c]+=dp[r+1][c+1]
        
        return dp[0][0]


"""
    c   a   a   a   t
c   
a                  0 
t   1    1   1  1   1
"""
        