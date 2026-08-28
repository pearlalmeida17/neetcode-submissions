import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        result = 0 

        stack = []

        ops = {
            "+" : operator.add,
            "-" : operator.sub,
            "*" : operator.mul,
            "/" : lambda a, b : int(a/b)
        }

        for token in tokens:
            if str(token) in ops and stack:
                b = stack.pop()
                a = stack.pop()
                
                result = ops[token](a, b)
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack.pop()




        