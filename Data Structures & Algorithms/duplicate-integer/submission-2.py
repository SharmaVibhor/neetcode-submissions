class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        maps = set()

        for i in range(0,len(nums)):
            if nums[i] in maps:
                return True
            else:
                maps.add(nums[i])

        return False
        