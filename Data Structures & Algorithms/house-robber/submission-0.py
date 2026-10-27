class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [None] * n

        def memoization(i):
            if i > n or i == n:
                return 0
            
            if cache[i] is not None:
                return cache[i]
            else:
                cache[i] = max(nums[i] + memoization(i + 2), memoization(i + 1))
                return cache[i]
        
        return memoization(0)