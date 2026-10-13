class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        subset = []

        def backtrack(index,sum):
            if sum == target:
                result.append(subset.copy())
                return

            if sum > target or index >= len(candidates):
                return

            subset.append(candidates[index])
            backtrack(index+1,candidates[index] + sum)
            subset.pop()

            while index +1<len(candidates) and candidates[index]==candidates[index+1]:
                index+=1
            backtrack(index+1,sum)

        backtrack(0,0)
        return result
        