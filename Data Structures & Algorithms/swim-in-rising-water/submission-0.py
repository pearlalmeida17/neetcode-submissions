import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row = len(grid)
        cols = len(grid[0])

        matrix = [[float('inf') for r in range(row)] for r in range(cols)]

        min_heap = []
        heapq.heappush(min_heap, (grid[0][0], 0, 0))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dijkstra(i, j):       
            while min_heap: 
                min_t, r, c = heapq.heappop(min_heap)

                if r == row - 1 and c == cols - 1:
                    return min_t

                if min_t > matrix[r][c] :
                    continue
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if  0 <= nr < row  and 0 <= nc < cols:
                        

                        new_t = max(grid[nr][nc], min_t)
                        if new_t < matrix[nr][nc]:
                            matrix[nr][nc] = new_t
                            heapq.heappush(min_heap, (new_t, nr, nc ))

                        

        return dijkstra(0,0)


                





        