from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        visited = [False] * len(nums)

        def backtrack():
            # Base Case: complete permutation formed
            if len(sol) == len(nums):
                res.append(sol.copy())
                return

            # Try picking every available number
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    sol.append(nums[i])

                    backtrack()

                    # Backtrack step
                    sol.pop()
                    visited[i] = False

        backtrack()
        return res