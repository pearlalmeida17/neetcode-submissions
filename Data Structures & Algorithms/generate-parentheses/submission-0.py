class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        parsubset = []


        def backtrack(open, close):
            if open == n and close == n:
                res.append("".join(parsubset))
                return

            
            if open < n:
                parsubset.append("(")
                backtrack(open + 1, close)
                parsubset.pop()
            
            if close < open :
                parsubset.append(")")
                backtrack(open, close + 1)
                parsubset.pop()
            
        backtrack(0,0)
        return res


            



        