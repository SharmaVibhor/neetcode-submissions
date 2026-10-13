class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])

        res = []

        for interval in intervals:
            if not res:
                res.append(interval)
                continue
            
            temp = res[-1]

            if interval[0]<=temp[1]:
                res[-1] = [min(temp[0],interval[0]), max(temp[1],interval[1])]
            else:
                res.append(interval)
        
        return res
        