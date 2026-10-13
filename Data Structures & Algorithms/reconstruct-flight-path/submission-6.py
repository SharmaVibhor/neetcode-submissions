class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #generate adjacency list
        adj = defaultdict(list)

        for src,des in sorted(tickets, reverse = True):
            adj[src].append(des)

        # Need to do DFS with backtracking
        res = [ ]

        def dfs(src):
            while adj[src]: 
                v = adj[src].pop()
                dfs(v)
            res.append(src)
        dfs("JFK")
        
        return res[::-1]