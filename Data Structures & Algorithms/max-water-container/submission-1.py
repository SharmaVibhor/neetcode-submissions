class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        start =0
        end = len(heights)-1

        while(start<end):
            vol = min(heights[start],heights[end])*(end-start)
            print(vol)
            res = max(res,vol)

            if heights[start]<heights[end]:
                start+=1
            else:
                end=end-1
        
        return res
        