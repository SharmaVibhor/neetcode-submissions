class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = [0]*n
        cache[n-1] = cost[n-1]
        cache[n-2] = cost[n-2]

        for i in range(n-3,-1,-1):
            cache[i] = cost[i] + min(cache[i+1],cache[i+2])

        return min(cache[0],cache[1])
        