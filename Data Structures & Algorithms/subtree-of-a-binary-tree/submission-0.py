# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(root,subroot):
            if not root and not subroot:
                return True

            if root and subroot and root.val == subroot.val:
                return isSameTree(root.left,subroot.left) and isSameTree(root.right,subroot.right)
            else :
                return False
        
        if not subRoot:
            return True

        if not root and subRoot:
            return False
        
        if root.val == subRoot.val and isSameTree(root,subRoot):
            return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
                
        