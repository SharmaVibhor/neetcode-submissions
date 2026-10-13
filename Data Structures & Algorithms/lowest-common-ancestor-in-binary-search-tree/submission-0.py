# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        left = TreeNode()
        right = TreeNode()

        if(p.val < q.val):
            left = p
            right = q
        else:
            left = q
            right = p
        
        if (left.val <= root.val and root.val <= right.val):
            return root
        
        elif(left.val < root.val and root.val > right.val):
            return self.lowestCommonAncestor(root.left,p,q)

        else:
            return self.lowestCommonAncestor(root.right,p,q)



        