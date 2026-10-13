class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        minSum, curMin = nums[0],0
        maxSum, curMax = nums[0],0
        total = 0

        for n in nums:
            curMin = min(n,curMin+n)
            curMax = max(n, curMax+n)

            total += n
            minSum = min(minSum,curMin)
            maxSum = max(maxSum,curMax)
        
        return max(maxSum,(total - minSum)) if maxSum>0 else maxSum