class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = {}
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def dfs(r,c,val):
            if r<0 or c<0 or r>=ROWS or c >=COLS or matrix[r][c]<=val:
                return 0
            
            if (r,c) in dp:
                return dp[(r,c)]

            res = 1

            for dr,dc in directions:
                new_r,new_c = r+dr,c+dc
                res = max(res,1+dfs(new_r,new_c,matrix[r][c]))
            
            dp[(r,c)]=res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,-1)
        
        return max(dp.values())