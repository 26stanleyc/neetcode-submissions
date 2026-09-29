class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d = []
        for i in range(len(position)):
            d.append((position[i], speed[i]))
        st = deque()
        d = sorted(d, reverse=True)
        for x, y in d:
            time = (target-x)/y
            if(not st):
                st.append(time)
            else:
                if(time > st[-1]):
                    st.append(time)
        return len(st)


            