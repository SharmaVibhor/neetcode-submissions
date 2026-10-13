class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        result = 0

        rightIndex = len(prices) - 1
        maxRight = prices[rightIndex]

        while rightIndex > 0:
            rightIndex -= 1
            profit = maxRight - prices[rightIndex]

            if profit > result:
                result = profit
            
            maxRight = max(maxRight, prices[rightIndex])

        return result

        