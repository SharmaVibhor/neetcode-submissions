class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        r = max(piles)
        l = 1

        result = r

        while l<=r:
            m = (l + r)//2

            hours = 0

            for i in piles :
                div = i // m
                mod = i % m

                hours += div
                if (mod != 0):
                    hours +=1
            
            if hours <= h:
                result = min(result,m)
                r = m -1

            else:
                l = m+1
        
        return result


        