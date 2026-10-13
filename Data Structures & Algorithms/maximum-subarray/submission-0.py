class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -math.inf
        sum = 0

        for i in range(len(nums)):
            sum+=nums[i]

            if(sum>res):
                res = sum
            if sum<0:
                sum = 0
        
        return res
        