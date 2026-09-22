import heapq
from collections import Counter, deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)

        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)

        q = deque()

        time = 0

        while max_heap or q:
            time += 1

            if q and q[0][1] == time:
                ready_cnt, _ = q.popleft()
                heapq.heappush(max_heap, ready_cnt)

            if max_heap:

                cnt = heapq.heappop(max_heap) + 1

                if cnt !=0:
                    q.append((cnt, time + n + 1))

        return time
                
        