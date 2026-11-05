from collections import deque
from typing import Optional

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        d = deque()
        curr = root
        c = 0
        while curr is not None or d:
            if curr is not None:
                # still descending: save this node and go left
                d.append(curr)
                curr = curr.left
            else:
                # hit the bottom: visit the next node in order
                curr = d.pop()
                c += 1
                if c == k:
                    return curr.val
                # then explore its right subtree
                curr = curr.right
            