class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []

        def backtrack(openN,close): 
            if openN == close == n:
                res.append("".join(subset))
                return

            if openN<n:
                subset.append("(")
                backtrack(openN+1,close)
                subset.pop()
            if close<openN:
                subset.append(")")
                backtrack(openN,close+1)
                subset.pop()
        
        backtrack(0,0)
        return res
        