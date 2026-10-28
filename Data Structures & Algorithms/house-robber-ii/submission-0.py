class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def robber(sub_nums):
            n = len(sub_nums)
            cache = [None] * n

            def memoization(i):
                if i >= n :
                    return 0
                if cache[i] is not None:
                    return cache[i]
                else:
                    cache[i] = max(sub_nums[i] + memoization(i + 2), memoization(i + 1)) 
                    return cache[i]
            
            return memoization(0)
        
        return max(robber(nums[:-1]), robber(nums[1:]))

        