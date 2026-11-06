class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {v: i for i, v in enumerate(inorder)}
        self.pre_idx = 0

        def build(lo, hi):                   # inorder[lo..hi]
            if lo > hi:
                return None
            val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(val)
            mid = pos[val]
            root.left = build(lo, mid - 1)   # must build left first
            root.right = build(mid + 1, hi)
            return root

        return build(0, len(inorder) - 1)