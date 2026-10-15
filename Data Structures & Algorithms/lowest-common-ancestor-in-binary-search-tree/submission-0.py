# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def contain(root, value):
            if(root == None):
                return False
            if(root.val == value):
                return True
            return contain(root.left, value) or contain(root.right, value)
        if(p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        elif(p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
        