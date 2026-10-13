class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxSoFar = 1
        minSoFar = 1
        res = nums[0]

        for num in nums:
            temp = num*maxSoFar
            maxSoFar = max(temp, num*minSoFar, num)
            minSoFar = min(temp, num*minSoFar, num)

            if maxSoFar>res:
                res = maxSoFar

            if num==0:
                minSoFar = 1
                maxSoFar = 1
        
        return res
        