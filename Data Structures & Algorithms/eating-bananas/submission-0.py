import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        l, r = 1, max(piles) 

        while l <= r :
             
            k = (l + r) // 2

            total_hours = sum(math.ceil(p/k) for p in piles)

            if total_hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        
        return res




        