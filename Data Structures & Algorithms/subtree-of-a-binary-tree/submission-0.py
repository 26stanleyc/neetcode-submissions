# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(self, a, b):
            if(a == None and b == None):
                return True
            elif(a == None or b == None):
                return False
            if(a.val != b.val):
                return False
            return same(self, a.left, b.left) and same(self, a.right, b.right)
        if(root==None):
            return False
        if(same(self, root, subRoot)):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)