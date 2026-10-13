class Solution:
    def search(self, nums: List[int], target: int) -> int:

        leftIndex = 0
        rightIndex = len(nums)
        res = -1

        while leftIndex < rightIndex :
            center = int((rightIndex + leftIndex)/2)

            if nums[center] == target:
                res = center 
                break
            
            elif nums[center] < target:
                leftIndex = center + 1

            else:
                rightIndex = center
        
        return res
        