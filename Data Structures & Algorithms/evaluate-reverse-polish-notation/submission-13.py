class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = deque()
        for x in tokens:
            if(x == '+' or x == '-' or x == '*' or x == '/'):
                op1 = operators[-2]
                op2 = operators[-1]
                res = 0
                if(x == '+'):
                    res = op1 + op2
                elif(x == '-'):
                    res = op1 - op2
                elif(x == '*'):
                    res = op1 * op2
                else:
                    res = int(op1 / op2)
                operators.pop()
                operators.pop()
                operators.append(res)
            else:
                operators.append(int(x))
        return operators[0]
        