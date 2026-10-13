class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0],nums[1])

        def helper(nums):
            if len(nums)==1:
                return nums[0]

            prev = nums[0]
            cur = max(nums[1],prev)

            for i in range(2,len(nums)):
                temp = max(prev + nums[i],cur)
                prev = cur
                cur = temp

            return cur

        return max(helper(nums[1:]),helper(nums[:-1]))
        