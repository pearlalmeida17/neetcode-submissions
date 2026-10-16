import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        graph = defaultdict(list)

        for u,v,t in times:
            graph[u].append((v, t))

        min_time = []

        heapq.heappush(min_time, (0, k))

        while min_time:
            time, node = heapq.heappop(min_time)

            if time > dist[node]:
                continue

            for v, w in graph[node]:
                if (time + w) < dist[v]:
                    dist[v] = (time + w) 
                    heapq.heappush(min_time, (dist[v], v)) 
        
        max_dist = max(dist[1:])

        return max_dist if max_dist < float('inf') else -1


                




         
        