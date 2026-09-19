class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for x in strs:
            l = len(x)
            s+= str(l) + '#' + x
        return s
   

    def decode(self, s: str) -> List[str]:
        arr = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])   
            arr.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return arr



                
