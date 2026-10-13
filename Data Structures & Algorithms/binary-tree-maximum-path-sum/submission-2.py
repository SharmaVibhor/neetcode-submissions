# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -math.inf

        def dfs(root):
            if not root:
                return 0

            nonlocal res

            lmax = max(0,dfs(root.left))
            rmax = max(0,dfs(root.right))

            res = max(res, root.val+lmax+rmax)

            return root.val + max(lmax,rmax)


        dfs(root)
        return res
        