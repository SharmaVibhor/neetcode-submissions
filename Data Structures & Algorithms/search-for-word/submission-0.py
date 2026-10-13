class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        subset = []
        rows = len(board)
        cols = len(board[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()

        def backtrack(r,c,index):
            subset.append(board[r][c])
            
            if "".join(subset) == word:
                return True

            visited.add((r,c))
            for dr,dc in directions:
                nr,nc = r+dr,c+dc

                if(
                    nr<0 or nr>=rows or nc<0 or nc>=cols or (nr,nc) in visited or index>=len(word) or board[nr][nc]!=word[index]
                ):
                    continue

                if backtrack(nr,nc,index+1):
                    return True
            subset.pop()
            visited.remove((r,c))
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c]==word[0]:
                    subset.clear()
                    visited.clear()
                    if backtrack(r,c,1):
                        return True
        
        return False
        