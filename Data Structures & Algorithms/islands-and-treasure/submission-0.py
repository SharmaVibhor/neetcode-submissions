class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rows = len(grid)
        cols = len(grid[0])


        def bfs(r,c):
            queue = collections.deque()
            queue.append((r,c))
            distance = 1
            visited = [[False for _ in range(cols)] for _ in range(rows)]
            visited[r][c] = True

            while queue:
                for i in range(len(queue)):
                    r,c = queue.popleft()

                    for dr,dc in directions:
                        new_r,new_c =r+dr,c+dc

                        if(new_r<0 or new_r>=rows or new_c<0 or new_c>=cols or grid[new_r][new_c]== 0 or grid[new_r][new_c] == -1 or visited[new_r][new_c]):
                            continue
                        
                        queue.append((new_r,new_c))
                        visited[new_r][new_c] = True
                        grid[new_r][new_c] = min(grid[new_r][new_c],distance)
                distance +=1


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    bfs(r,c)
        