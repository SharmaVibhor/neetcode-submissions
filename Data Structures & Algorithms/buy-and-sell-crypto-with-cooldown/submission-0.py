class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0

        buy = -prices[0]
        sell = 0
        cd = 0

        for i in range(1,len(prices)):
            prevbuy = buy
            prevsell = sell
            prevcd = cd

            buy = max(prevbuy, prevcd-prices[i])
            sell = prevbuy+prices[i]
            cd = max(prevsell,prevcd)

        return max(cd,sell)
        