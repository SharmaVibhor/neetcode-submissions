class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False for _ in range(cols)] for _ in range(rows)]
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        maxArea = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and not visited[r][c]:
                    area = 1
                    stack = [(r,c)]
                    visited[r][c]=True

                    while stack:
                        row,col = stack.pop()

                        for x,y in directions:
                            nr,nc = row+x,col+y

                            if nr<0 or nr>=rows or nc<0 or nc>=cols or visited[nr][nc] or grid[nr][nc]==0:
                                continue
                            
                            visited[nr][nc]=True
                            stack.append((nr,nc))
                            area+=1
                    maxArea = max(maxArea,area)

        return maxArea
        