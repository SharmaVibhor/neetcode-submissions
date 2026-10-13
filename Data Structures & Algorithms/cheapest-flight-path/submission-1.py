class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [100000]* n
        #adj = {i:[] for i in range(n)}
        prices[src] = 0 

        #for source,dest,cost in flights:
        #    adj[source].append([dest,cost])

        for i in range(0,k+1):
            temp = prices.copy()

            for s,d,c in flights:
                temp[d] = min(temp[d], prices[s]+c)
            
            prices = temp
        
        return prices[dst] if prices[dst] <100000 else -1

        