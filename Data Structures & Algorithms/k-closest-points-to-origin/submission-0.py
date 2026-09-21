import math, heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for i in range(len(points)):
            xi = points[i][0]
            yi = points[i][1]

            dist = -math.sqrt((xi**2) + (yi**2))

            heapq.heappush(max_heap, (dist, [xi, yi]))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
            
        return [points for (dist, points) in max_heap]