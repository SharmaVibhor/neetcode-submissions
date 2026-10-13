class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        last_val = 100000

        for r in range(1,len(nums)):
            if nums[r]!=nums[r-1]:
                nums[l] = nums[r]
                l +=1
            elif nums[r] == nums[r-1] and nums[r]!=last_val:
                nums[l] = nums[r]
                l += 1
                last_val = nums[r]
        
        return l
        