class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def helper(cap):
            temp = 0
            res = 1

            for w in weights:
                if temp+w <= cap:
                    temp+=w
                else:
                    res +=1
                    temp = w
            
            return res <= days
    
        l = max(weights)
        r = sum(weights)

        while l < r:
            mid = (l+r)//2

            if helper(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
        