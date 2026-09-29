from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()
        for x in s:
            if(x == '(' or x == "{" or x == "["):
                st.append(x)
            else:
                if(not st):
                    return False
                if(x == ')' and st[-1]!='('):
                    return False
                elif(x == '}' and st[-1]!='{'):
                    return False
                elif(x == ']' and st[-1]!='['):
                    return False
                st.pop()
        if(not st):
            return True
        return False
                    
        