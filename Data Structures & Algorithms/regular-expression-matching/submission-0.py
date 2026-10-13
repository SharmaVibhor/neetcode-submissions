class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(s) + 1)]
              for _ in range(len(p) + 1)]

        dp[len(p)][len(s)] = True

        for r in range(len(p) - 1, -1, -1):
            for c in range(len(s), -1, -1):

                first_match = (
                    c < len(s)
                    and (p[r] == s[c] or p[r] == ".")
                )

                if r + 1 < len(p) and p[r + 1] == "*":
                    dp[r][c] = (
                        dp[r + 2][c]
                        or
                        (first_match and dp[r][c + 1])
                    )
                else:
                    if c < len(s):
                        dp[r][c] = first_match and dp[r + 1][c + 1]

        return dp[0][0]
        