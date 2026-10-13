class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minHeap = [[grid[0][0],0,0]]
        visit = set((0,0))
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while minHeap:
            cost,row,col = heapq.heappop(minHeap)

            if row == col == N-1:
                return cost
            
            for x,y in directions:
                nr,nc = row +x, col+y

                if (nr,nc) not in visit and 0<= nr < N and 0<=nc <N:
                    heapq.heappush(minHeap,[max(cost,grid[nr][nc]),nr,nc])
                    visit.add((nr,nc))
        