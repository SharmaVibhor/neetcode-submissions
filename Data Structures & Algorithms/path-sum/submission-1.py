# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        def dfs(node, sumsofar):
            sumsofar += node.val

            if sumsofar == targetSum and not node.left and not node.right:
                return True
            
            if node.left and dfs(node.left,sumsofar):
                return True
            
            if node.right and dfs(node.right,sumsofar):
                return True
            
            return False
        

        return dfs(root,0)
            

            
            
        