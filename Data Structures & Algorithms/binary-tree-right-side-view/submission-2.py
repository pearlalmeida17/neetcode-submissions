# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def bfs(node:Optional[TreeNode], depth: int):

            if not node:
                return 
            
            if depth == len(res):
                res.append(node.val)
            
            bfs(node.right, depth + 1)
            bfs(node.left, depth + 1)
        
        bfs(root,0)
    
        return res
        