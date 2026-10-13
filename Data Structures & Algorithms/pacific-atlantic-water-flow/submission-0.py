class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols=len(heights),len(heights[0])
        res = []
        pac,atl = set(),set()
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(r,c,visit,prevHeight):
            if((r,c) in visit or r<0 or c<0 or r>=rows or c>=cols or heights[r][c]<prevHeight):
                return
            
            visit.add((r,c))
            for x,y in directions:
                nr,nc = r+x,c+y
                dfs(nr,nc,visit,heights[r][c])

        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])

        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])
        
        return list(pac & atl)
        


        