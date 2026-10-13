class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cursum = 0
        prefix = defaultdict(int)
        prefix[0] = 1

        for num in nums:
            cursum +=num

            if cursum - k in prefix:
                res +=prefix[cursum-k]

            prefix[cursum]+=1
        
        return res
        