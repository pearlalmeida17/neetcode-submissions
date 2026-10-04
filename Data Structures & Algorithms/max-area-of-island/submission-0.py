class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        row_len, col_len = len(grid), len(grid[0])
        island_area = 0
        island_count = 0

        def dfs(row:int, col: int) -> int:
            if row < 0 or row >= row_len or col < 0 or col >= col_len or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0

            return (
            1 
            + dfs(row - 1, col)
            + dfs(row + 1, col)
            + dfs(row, col - 1)
            + dfs(row, col + 1)
            )

        
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 1:
                    island_count = dfs(r, c)
                    island_area = max(island_area, island_count)

        return island_area