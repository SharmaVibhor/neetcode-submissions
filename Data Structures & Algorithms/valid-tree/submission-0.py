class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        visited = set()

        def dfs(node,par):
            if node in visited:
                return False

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == par:
                    continue
                if not dfs(neighbor,node):
                    return False
            return True

        return dfs(0,-1) and len(visited) == n

        
        