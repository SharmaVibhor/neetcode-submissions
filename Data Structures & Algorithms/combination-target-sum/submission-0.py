class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(index, sum):
            if sum == target:
                result.append(subset.copy())
                return
            
            if sum>target or index>=len(nums):
                return

            subset.append(nums[index])
            backtrack(index, sum + nums[index])
            subset.pop()
            backtrack(index+1, sum)

        backtrack(0,0)
        return result

            
        