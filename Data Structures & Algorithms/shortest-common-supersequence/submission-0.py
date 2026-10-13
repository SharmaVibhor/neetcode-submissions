class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [[0]* (len(str1)+1) for _ in range(len(str2)+1)]

        for i in range(len(str1)-1,-1,-1):
            dp[len(str2)][i] = 1 + dp[len(str2)][i+1]
        
        for i in range(len(str2)-1,-1,-1):
            dp[i][len(str1)] = 1+dp[i+1][len(str1)]

        for r in range(len(str2)-1,-1,-1):
            for c in range(len(str1)-1,-1,-1):
                if str2[r] == str1[c]:
                    dp[r][c] = 1 + dp[r+1][c+1]
                else:
                    dp[r][c] = 1 + min(dp[r+1][c],dp[r][c+1])
        
        r = 0
        c = 0
        res = []

        while r < len(str2) and c < len(str1):
            if str2[r] == str1[c]:
                res.append(str2[r])
                r+=1
                c+=1
            elif dp[r+1][c] < dp[r][c+1]:
                res.append(str2[r])
                r+=1
            else:
                res.append(str1[c])
                c+=1
        
        if r < len(str2):
            res.append(str2[r:])
        
        if c < len(str1):
            res.append(str1[c:])
        
        return "".join(res)       