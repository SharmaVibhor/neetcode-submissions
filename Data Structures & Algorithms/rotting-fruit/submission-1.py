class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        q = deque()
        visited =[[False for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                    visited[r][c]=True
        
        while q:
            r,c = q.popleft()

            for x,y in directions:
                nr,nc = r+x,c+y

                if nr<0 or nr>=rows or nc<0 or nc>=cols or grid[nr][nc]==0 or visited[nr][nc]:
                    continue
                
                visited[nr][nc]=True
                q.append((nr,nc))
                grid[nr][nc]= grid[nr][nc] + grid[r][c]

        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    return -1
                elif grid[r][c]==2:
                    continue
                res = max(res, grid[r][c]-2)

        return res

                    