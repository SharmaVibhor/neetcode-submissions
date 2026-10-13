class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftIndex = 0
        rightIndex = len(heights) -1
        area = 0

        while leftIndex < rightIndex:
            newArea = min(heights[leftIndex],heights[rightIndex]) * (rightIndex - leftIndex)
            if newArea > area:
                area = newArea
            
            if heights[leftIndex] < heights[rightIndex]:
                leftIndex +=1
            else:
                rightIndex-=1
        
        return area


        