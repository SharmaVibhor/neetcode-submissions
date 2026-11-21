class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def helper(p1turn,start,end):
            if start > end:
                return 0
            
            if (p1turn,start,end) in dp:
                return dp[(p1turn,start,end)]
            
            res = 0 if p1turn else 1e9

            if p1turn:
                pick_left = piles[start] + helper(not p1turn, start + 1, end)
                pick_right = piles[end] + helper(not p1turn, start, end - 1)
                res = max(pick_left, pick_right)
            else:
                pick_left = helper(not p1turn, start + 1, end)
                pick_right = helper(not p1turn, start, end - 1)
                res = min(pick_left, pick_right)
            dp[(p1turn,start,end)] = res
            return res

        p1score = helper(True,0,len(piles)-1)
        p2score = sum(piles) - p1score

        return p1score > p2score
        