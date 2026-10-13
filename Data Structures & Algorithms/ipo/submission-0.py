class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pairs = [(capital[i],profits[i]) for i in range(len(capital))]
        pairs.sort()
        maxHeap = []
        res = 0
        res+=w

        for cap, prof in pairs:
            if cap <= w:
                heapq.heappush_max(maxHeap,(prof,cap))
                continue
            
            while k and maxHeap and cap>w:
                cur_prof,cur_w = heapq.heappop_max(maxHeap)
                res+=cur_prof
                w+=cur_prof
                k-=1
            
            if cap<=w:
                heapq.heappush_max(maxHeap,(prof,cap))
        
        while k and maxHeap:
            prof,_ = heapq.heappop_max(maxHeap)
            res+=prof
            k-=1
        
        return res