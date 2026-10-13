class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]

        for i,num in enumerate(nums):
            if num>0:
                break
            if i>0 and num == nums[i-1]:
                continue

            l,r = i+1, len(nums)-1
            while l<r:
                if num + nums[l] + nums[r] > 0:
                    r = r-1
                elif num + nums[l] + nums[r] < 0:
                    l=l+1
                else:
                    res.append([num,nums[l],nums[r]])
                    l=l+1
                    r=r-1
                    while l<r and nums[l]==nums[l-1]:
                        l=l+1

        return res
        