class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        numlen = len(nums)
        left = [1]*numlen
        right = [1]*numlen
        res = [1]*numlen

        left[0] = 1
        right[numlen-1] = 1

        for i in range(1,numlen):
            left[i] = nums[i-1]*left[i-1]
            right[numlen-i-1] = nums[numlen-i]*right[numlen-i]

        for i in range(numlen):
            res[i] = left[i]*right[i]

        return res

        