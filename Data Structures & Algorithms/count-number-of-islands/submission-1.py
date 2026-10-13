class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        islands = 0
        directions =[[1,0],[-1,0],[0,1],[0,-1]]

        visited = [[False for _ in range(columns)] for _ in range(rows)]

        def bfs(r,c):
            queue = collections.deque()
            visited[r][c] = True

            queue.append((r,c))

            while queue:
                r,c = queue.popleft()
                for dr,dc in directions:
                    nr,nc = dr+r,dc+c

                    if(nr <0 or nc<0 or nr>=rows or nc>=columns or grid[nr][nc]=="0" or visited[nr][nc]):
                        continue
                    queue.append((nr,nc))
                    visited[nr][nc]=True

        for r in range(rows):
            for c in range(columns):
                if grid[r][c]=="1" and not visited[r][c]:
                    bfs(r,c)
                    islands +=1
        
        return islands
        