class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result=[]
        count=defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n]+=1

        for key,value in count.items():
            freq[value].append(key)

        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                result.append(n)
                if len(result)==k:
                    return result
        