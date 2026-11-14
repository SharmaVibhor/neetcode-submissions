class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}

        for c in s:
            freq[c] = 1 + freq.get(c,0)
        
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        if sorted_items[0][1] > (len(s)+1)//2:
            return ""

        res = [None]*len(s)
        i = 0

        for c,count in sorted_items:
            for _ in range(count):
                res[i] = c
                i+=2
                if i>=len(s) and i%2 == 0:
                    i = 1
        
        return "".join(res)  