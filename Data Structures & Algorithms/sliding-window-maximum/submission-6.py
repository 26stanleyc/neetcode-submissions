from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()   # indices; nums values decrease from front to back
        res = []

        for i, x in enumerate(nums):
            # 1. drop smaller (or equal) elements from the back: they can never be the max now
            while dq and nums[dq[-1]] <= x:
                dq.pop()

            # 2. add the current index
            dq.append(i)

            # 3. drop the front if it has slid out of the window
            if dq[0] <= i - k:
                dq.popleft()

            # 4. once the first full window is formed, the front is the max
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res