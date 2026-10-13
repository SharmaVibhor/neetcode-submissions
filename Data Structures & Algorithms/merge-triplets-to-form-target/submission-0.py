class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [-1,-1,-1]

        for a,b,c in triplets:
            if a<=target[0] and b<=target[1] and c<=target[2]:
                res[0],res[1],res[2] = max(res[0],a),max(res[1],b),max(res[2],c)
            
        return res == target
        