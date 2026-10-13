class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for p in points:
            dist = math.sqrt(p[0]*p[0] + p[1]*p[1])
            heapq.heappush_max(max_heap,[dist,p[0],p[1]])

            if len(max_heap)>k:
                heapq.heappop_max(max_heap)

        res = []

        for d,x,y in max_heap:
            res.append([x,y])
        
        return res
        