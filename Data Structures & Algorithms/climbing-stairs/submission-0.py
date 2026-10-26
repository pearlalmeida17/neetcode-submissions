class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [None] * n

        def memoization(i):
            if i > n:
                return 0

            if i == n:
                return 1
            
            if cache[i] is not None:
                return cache[i]
            else:
                cache[i] = memoization(i + 1) + memoization(i + 2)
                return cache[i]
        

        return memoization(0)
        