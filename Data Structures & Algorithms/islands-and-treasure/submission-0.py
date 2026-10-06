from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return 

        row_len = len(grid)
        col_len = len(grid[0])

        treasure = deque()

        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 0:
                    treasure.append((r, c))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while treasure:

            r, c = treasure.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < row_len and 0<= nc < col_len and grid[nr][nc] == 2147483647:
                    
                    grid[nr][nc] = grid[r][c] + 1
                    treasure.append((nr, nc))






        

        