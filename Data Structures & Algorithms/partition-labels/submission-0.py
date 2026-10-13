class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i,c in enumerate(s):
            lastIndex[c]=i

        res = []

        r=0
        size = 0

        for i,c in enumerate(s):
            size+=1
            r = max(r,lastIndex[c])

            if i== r:
                res.append(size)
                size = 0


        return res
        