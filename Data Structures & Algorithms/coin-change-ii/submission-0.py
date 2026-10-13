class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1

        for c in coins:
            temp = [0]*(amount+1)
            temp[0]=1
            for i in range(1,amount+1):
                temp[i] = dp[i]
                if i-c>=0:
                    temp[i] += temp[i-c]
            
            dp = temp
        
        return dp[amount]
                