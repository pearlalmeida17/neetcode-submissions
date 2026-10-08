class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic = set()
        pacific = set()

        res = []

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        row_len = len(heights)
        col_len = len(heights[0])

        def dfs(r, c, ocean_set):
            ocean_set.add((r,c))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if (0 <= nr < row_len) and (0 <= nc < col_len)and (nr, nc) not in ocean_set and heights[r][c] <= heights[nr][nc]:
                    dfs(nr, nc, ocean_set)


        for r in range(row_len):
            dfs(r, 0, pacific)
        for c in range(col_len):
            dfs(0, c, pacific)

        for r in range(row_len):
            dfs(r, col_len -1, atlantic)
        for c in range(col_len):
            dfs(row_len -1, c, atlantic)
        
        for r in range(row_len):
            for c in range(col_len):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append((r,c))
        
        return res


            
                 
            

