# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        def helper(root, x):
            if root is None:
                return 0
            if(root.val >= x):
                return 1 + helper(root.left, root.val) + helper(root.right, root.val)
            else:
                return helper(root.left, x) + helper(root.right, x)
        return helper(root, root.val)