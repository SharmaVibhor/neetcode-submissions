class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1]*(len(edges)+1)
        visited = set()

        def find(node):
            res = node
            while res!=parent[res]:
                parent[res]=parent[parent[res]]
                res = parent[res]
            return res

        def union(node1,node2):
            p1,p2 = find(node1),find(node2)
            if p1 == p2:
                return 0

            if rank[p1]>rank[p2]:
                parent[p2] = p1
                rank[p1]+=rank[p2]
            else:
                parent[p1] = p2
                rank[p2]+=rank[p1]
            return 1

        for n1,n2 in edges:
            merge = union(n1,n2)
            if not merge:
                return [n1,n2]
            

        