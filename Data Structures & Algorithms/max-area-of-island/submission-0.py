class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False for _ in range(cols)] for _ in range(rows)]
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        maxArea = 0

        def bfs(r,c):
            queue = collections.deque()
            queue.append((r,c))
            visited[r][c] = True
            area = 1 
            nonlocal maxArea

            while queue:
                r,c = queue.popleft()

                for dr,dc in directions:
                    cur_r,cur_c = dr + r, dc + c

                    if (cur_r <0 or cur_r>=rows or cur_c <0 or cur_c>=cols or grid[cur_r][cur_c] == 0 or visited[cur_r][cur_c]):
                        continue
                    queue.append((cur_r,cur_c))
                    visited[cur_r][cur_c]=True
                    area +=1
            print(area)
            maxArea = max(maxArea,area)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and not visited[r][c]:
                    bfs(r,c)

        return maxArea
        