class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        dp = {}

        def dfs(i,zeros,ones):
            if zeros > m or ones >n:
                return -10000
            
            if i == len(strs):
                return 0
            
            if (i,zeros,ones) in dp:
                return dp[(i,zeros,ones)]
            
            z = strs[i].count("0")
            o = strs[i].count("1")
            
            dp[(i,zeros,ones)] = max(dfs(i+1,zeros,ones), dfs(i+1,zeros+z,ones+o) + 1)

            return dp[(i,zeros,ones)]

        return dfs(0,0,0)

        