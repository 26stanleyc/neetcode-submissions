class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        dicti = {}
        for x in s1:
            dicti[x] = dicti.get(x, 0) + 1
        print(dicti)
        sol = {}
        for right, value in enumerate(s2):
            if value in dicti:
                sol[value] = sol.get(value, 0) + 1
            if right >= len(s1):
                out = s2[right - len(s1)]
                if out in dicti:
                    sol[out] -= 1
                    if sol[out] == 0:
                        del sol[out]

            if sol == dicti:
                return True

        return False
                    

        
