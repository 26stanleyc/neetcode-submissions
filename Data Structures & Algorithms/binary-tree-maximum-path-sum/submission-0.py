# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root):
        best = float('-inf')

        def gain(node):
            nonlocal best
            if not node:
                return 0
            left = max(gain(node.left), 0)    # ignore negative branches
            right = max(gain(node.right), 0)
            best = max(best, node.val + left + right)  # path that bends here
            return node.val + max(left, right)         # path that continues up
        
        gain(root)
        return best