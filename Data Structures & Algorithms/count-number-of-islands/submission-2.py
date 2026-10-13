class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        islands = 0
        directions =[[1,0],[-1,0],[0,1],[0,-1]]

        visited = set()
        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c]=="1" and (r,c) not in visited:
                    islands+=1

                    visited.add((r,c))
                    stack=[(r,c)]

                    while stack:
                        row, col = stack.pop()

                        for x,y in directions:
                            nr,nc = row+x,col+y

                            if nr<0 or nr>=rows or nc<0 or nc>=columns or (nr,nc) in visited or grid[nr][nc]=="0":
                                continue
                            visited.add((nr,nc))
                            stack.append((nr,nc))



        
        return islands
        