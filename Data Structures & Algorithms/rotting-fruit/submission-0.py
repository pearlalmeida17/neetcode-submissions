from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        
        fresh_count = 0
        row_len = len(grid)
        col_len = len(grid[0])

        queue = deque()

        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue and fresh_count > 0:
            
            minutes += 1
            

            for _ in range(len(queue)):
                r, c = queue.popleft() 

                for dr, dc in directions:
                    nr , nc = dr + r, dc + c

                    if 0 <= nr < row_len and 0 <= nc < col_len and grid[nr][nc] == 1:
                        fresh_count -= 1
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                     
        return minutes if fresh_count == 0 else -1


        
                    
