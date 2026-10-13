class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        prev = nums[0]
        cur = max(nums[1],prev)

        for i in range(2,len(nums)):
            temp = max(prev + nums[i],cur)
            prev = cur
            cur = temp

        return cur
        