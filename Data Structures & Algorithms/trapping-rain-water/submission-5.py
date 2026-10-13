class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0]*n
        right = [0]*n
        res = 0
        left[0] = height[0]
        right[n-1] = height[n-1]

        for i in range (1,n):
            if(height[i]>left[i-1]):
                left[i] = height[i]
            else:
                left[i] = left[i-1]

        for i in range(n-2,0,-1):
            if(height[i]>right[i+1]):
                right[i] = height[i]
            else:
                right[i] = right[i+1] 

        for i in range(1,n-1):
            res+=(min(left[i],right[i]) - height[i])
            print(min(left[i],right[i]) - height[i])

        #print(left)
        #print(right)
        return res
        