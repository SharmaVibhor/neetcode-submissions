class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0

        hashmap = defaultdict(int)

        for n in set(nums):
            if True:
                hashmap[n] = 1+ hashmap[n-1] + hashmap[n+1]
                print(hashmap)
                hashmap[n - hashmap[n-1]] = hashmap[n]
                hashmap[n+ hashmap[n+1]] = hashmap[n]
                if hashmap[n]>result:
                    result = hashmap[n]

        return result
        