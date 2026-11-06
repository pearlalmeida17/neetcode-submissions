class Solution:
    def numDecodings(self, s: str) -> int:

        cache = {}

        def memoization(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0

            if i in cache:
                return cache[i]
            
            res = memoization(i + 1)

            if i + 1 < len(s) and int(s[i : i + 2]) <= 26:
                res += memoization(i + 2)
            
            cache[i] = res
            return res
            
                
        return memoization(0)


        