class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while i!=nums[i]-1 and nums[i]>0 and nums[i]<=len(nums) and nums[i]!=nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        
        res = 1

        for i in range(len(nums)):
            if nums[i] == i+1:
                res+=1
            else:
                break
        
        return res

        