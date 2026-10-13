class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0

        for num in nums:
            total+=num

        if total%2:
            return False

        target = (total//2)

        dp = set()
        dp.add(0)

        for i in range (len(nums)-1,-1,-1):
            newdp = dp.copy()

            for element in dp:
                if(element + nums[i] == target):
                    return True
                newdp.add(element + nums[i])

            dp = newdp

        return True if target in dp else False

        