class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0

        curInterval = 0

        for interval in intervals:
            if not curInterval:
                curInterval = interval[1]
                continue

            if interval[0]<curInterval:
                res +=1 
                curInterval = min(interval[1],curInterval)
            else:
                curInterval = interval[1]
        
        return res


        