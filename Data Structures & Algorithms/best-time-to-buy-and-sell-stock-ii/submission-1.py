class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cur = prices[0]

        for i in range(1,len(prices)):
            if prices[i]>cur:
                res += prices[i] - cur    
            cur = prices[i]
        
        return res