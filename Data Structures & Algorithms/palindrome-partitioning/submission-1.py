

class Solution:

    def partition(self, s: str) -> List[List[str]]:
        res = []
        temp = []

        def is_palindrom(sub: str):
            return sub == sub[::-1]

        def backtrack(j):
            
            if j == len(s):
                res.append(temp.copy())
            
            for i in range(j + 1, len(s) + 1):
                sub = s[j:i]

                if is_palindrom(sub):
                    temp.append(sub)
                    backtrack(i)
                    temp.pop()
            
        backtrack(0)

        return res


            
        