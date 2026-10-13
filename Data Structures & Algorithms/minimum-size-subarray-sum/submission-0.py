class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = 100000
        sum = 0

        for r in range(len(nums)):
            sum += nums[r]

            while sum>= target:
                res = min(res,r-l+1)
                sum = sum - nums[l]
                l+=1
        
        return res if res!=100000 else 0
        