class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {i:0 for i in set(nums)}
        res = []

        for num in nums:
            count[num] +=1
        
        for (k,v) in count.items():
            if v > len(nums)//3:
                res.append(k)
        
        return res
        