class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        cache = [None] * n

        def memoization(i):
            if i > n:
                return 0
            if i == n:
                return 0
            
            if cache[i] is not None:
                return cache[i]
            else:
                cache[i] = cost[i] + min(memoization(i + 1) , memoization(i + 2))
                return cache[i]
        
        return min(memoization(0), memoization(1))

    