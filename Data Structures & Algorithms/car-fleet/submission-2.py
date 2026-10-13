class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position,speed)]
        res = []

        for p,s in sorted(pair)[::-1]:
            res.append((target - p)/s)
            if len(res) > 1 and res[-1]<=res[-2]:
                res.pop()
        
        return len(res)
        