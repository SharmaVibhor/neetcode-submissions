class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [1e9]*(n+1)
        dp[0] = 0
        durations = [1,7,30]
        
        for i in range(1,n+1):
            for c in range(len(costs)):
                cost = costs[c]
                duration = durations[c]

                j = i-1
                while j>0 and days[i-1] - days[j-1] < duration:
                    j=j-1
                dp[i] = min(dp[i],dp[j]+cost)

        return dp[-1]        