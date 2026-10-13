class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pairs = [(capital[i],profits[i]) for i in range(len(capital))]
        pairs.sort()
        maxHeap = []

        for cap, prof in pairs:
            if cap <= w:
                heapq.heappush_max(maxHeap,prof)
                continue
            
            while k and maxHeap and cap>w:
                cur_prof = heapq.heappop_max(maxHeap)
                w+=cur_prof
                k-=1
            
            if cap<=w:
                heapq.heappush_max(maxHeap,prof)
        
        while k and maxHeap:
            prof = heapq.heappop_max(maxHeap)
            w+=prof
            k-=1
        
        return w