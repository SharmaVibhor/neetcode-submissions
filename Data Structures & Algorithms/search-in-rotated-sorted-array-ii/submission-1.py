class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) -1

        res = False

        while l<=r:
            m = (l + r)//2

            if(nums[m] == target):
                res = True
                break
            
            if (nums[m]>nums[l]):
                if(nums[l]<=target and target<nums[m]):
                    r = m-1
                else:
                    l = m+1
            elif nums[m]<nums[l] :
                if(nums[r]>= target and target > nums[m]):
                    l = m+1
                else:
                    r = m-1
            else:
                l+=1
        
        return res