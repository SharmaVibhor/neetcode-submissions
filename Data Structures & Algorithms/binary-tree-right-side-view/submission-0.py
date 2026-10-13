# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        queue = collections.deque()
        queue.append(root)

        while(queue):
            qlen = len(queue)
            level = []

            for i in range (qlen):
                temp = queue.popleft()
                if temp:
                    level.append(temp.val)
                    queue.append(temp.left)
                    queue.append(temp.right)
            if level:
                res.append(level[-1])
            
        return res
        