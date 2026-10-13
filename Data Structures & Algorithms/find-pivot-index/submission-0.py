class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = [0]*len(nums)
        right = [0]*len(nums)

        for i in range(1,len(nums)):
            left[i] += nums[i-1] + left[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            right[i]+=nums[i+1] + right[i+1]
        
        for i in range(len(nums)):
            if left[i] == right[i]:
                return i
        
        return -1
        