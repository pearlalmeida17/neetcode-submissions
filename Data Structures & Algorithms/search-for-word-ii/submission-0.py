class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
    
    
    def addWord(self, word: str) -> None:
        
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
        curr.word = word

class Solution:
     
   

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.addWord(word)

        res = []
        row_len, col_len = len(board), len(board[0])

        def dfs(row, col, parent):
            char = board[row][col]
            curr_node = parent.children[char]

            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None

            board[row][col] = "#"

            for dr, dc in [(-1, 0), (1,0), (0,-1), (0, 1)]:
                nr, nc = row + dr, col + dc

                if (0 <=nr < row_len and 0 <= nc < col_len) and board[nr][nc] in curr_node.children:
                    dfs(nr, nc, curr_node)
                
            board[row][col] = char

            if not curr_node.children:
                parent.children.pop(char)
        
        for r in range(row_len):
            for c in range(col_len):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return res
    
                

                

                


       

