class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols = len(board),len(board[0])
        visited = set()
        stack = []
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        for r in range(rows):
            if board[r][0] == 'O':
                stack.append((r,0))
                visited.add((r,0))
            if board[r][cols-1]=='O':
                stack.append((r,cols-1))
                visited.add((r,cols-1))
        
        for c in range(cols):
            if board[0][c] == 'O':
                stack.append((0,c))
                visited.add((0,c))
            if board[rows-1][c]=='O':
                stack.append((rows-1,c))
                visited.add((rows-1,c))

        while stack:
            row,col = stack.pop()

            for x,y in directions:
                nr,nc = row+x,col+y

                if nr<0 or nr>=rows or nc<0 or nc>=cols or (nr,nc) in visited or board[nr][nc]=='X':
                    continue
                stack.append((nr,nc))
                visited.add((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O' and (r,c) not in visited:
                    board[r][c]='X'

        