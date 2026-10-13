# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0

        def nodes(root,maxi):

            if not root:
                return 0

            val = max(root.val,maxi)
            if (root.val >= val):
                return 1 + nodes(root.left,val) + nodes(root.right,val)

            else:
                return nodes(root.left,val) + nodes(root.right,val)

        res = nodes(root,root.val)

        return res
        