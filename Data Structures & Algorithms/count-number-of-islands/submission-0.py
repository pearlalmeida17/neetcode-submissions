class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0 

        row_len, col_len = len(grid), len(grid[0])
        island_count = 0

        def dfs(row, col):

            if row < 0 or row >= row_len or col < 0 or col >= col_len or grid[row][col] == "0":
                return
            
            grid[row][col] = "0"

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == "1":
                    island_count += 1
                    dfs(r,c)

        return island_count