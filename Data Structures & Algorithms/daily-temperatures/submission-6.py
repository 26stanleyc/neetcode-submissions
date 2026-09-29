class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = deque()
        l = [0] * len(temperatures)
        for idx, value in enumerate(temperatures):
            if(not s):
                s.append((value, idx))
            else:
                while(s and value > s[-1][0]):
                    l[s[-1][1]] = idx - s[-1][1]
                    s.pop()
                s.append((value, idx))
        return l

