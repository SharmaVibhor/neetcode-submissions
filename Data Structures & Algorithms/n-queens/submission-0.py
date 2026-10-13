class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."]*n for i in range(n)]
        col = set()
        posD = set()
        negD = set()

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r+c) in posD or (r-c) in negD:
                    continue

                board[r][c]="Q"
                col.add(c)
                posD.add(r+c)
                negD.add(r-c)
                backtrack(r+1)

                board[r][c]="."
                col.remove(c)
                posD.remove(r+c)
                negD.remove(r-c)

        backtrack(0)

        return res


        