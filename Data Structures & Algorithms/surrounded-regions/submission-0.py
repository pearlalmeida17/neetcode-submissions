class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return 
        
        row_len = len(board)
        col_len = len(board[0])

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(r, c):

            if r < 0 or  r >= row_len or c < 0 or c >= col_len or board[r][c] != "O" :
                return 

            board[r][c] = "E"
            
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(row_len):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][col_len - 1] == "O":
                dfs(r, col_len - 1)
        
        for c in range(col_len):
            if board[0][c] == "O":
                dfs(0, c)
            if board[row_len-1][c] == "O":
                dfs(row_len - 1, c)
        
        for r in range(row_len):
            for c in range(col_len):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "E":
                    board[r][c] = "O"
            

