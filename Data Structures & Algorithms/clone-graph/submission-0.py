"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visit = {node:Node(node.val)}
        stack = []
        stack.append(node)
        while stack:
            temp = stack.pop()

            for n in temp.neighbors:
                if n not in visit:
                    visit[n]=Node(n.val)
                    stack.append(n)
                visit[temp].neighbors.append(visit[n])

        return visit[node]