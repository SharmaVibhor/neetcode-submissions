class Solution:
    def trap(self, height: List[int]) -> int:
        leftIndex = 0
        rightIndex = len(height) -1

        leftMax = height[0]
        rightMax = height[rightIndex]

        result = 0

        while leftIndex < rightIndex :
            if leftMax < rightMax:
                leftIndex +=1
                leftMax = max(leftMax,height[leftIndex])
                result += leftMax - height[leftIndex]

            else:
                rightIndex -= 1
                rightMax = max(rightMax,height[rightIndex])
                result += rightMax - height[rightIndex]

        return result
        