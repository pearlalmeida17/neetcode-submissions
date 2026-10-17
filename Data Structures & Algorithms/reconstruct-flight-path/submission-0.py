import heapq
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        directs = defaultdict(list)

        for src, dst in sorted(tickets, reverse=True):
            directs[src].append(dst)
        
        route = []
        
        def dfs(airport):

            while directs[airport]:
               next_airport =  directs[airport].pop()
               dfs(next_airport)
            
            route.append(airport)

        dfs("JFK")

        return route[::-1]