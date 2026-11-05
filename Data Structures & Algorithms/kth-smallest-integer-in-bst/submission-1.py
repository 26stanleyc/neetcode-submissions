from collections import deque
from typing import Optional

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        d = deque()
        curr = root
        c = 0
        while curr is not None or d:
            if(curr is not None):
                d.append(curr)
                curr = curr.left
            else:
                curr = d.pop()
                c+=1
                if(c == k):
                    return curr.val
                curr = curr.right