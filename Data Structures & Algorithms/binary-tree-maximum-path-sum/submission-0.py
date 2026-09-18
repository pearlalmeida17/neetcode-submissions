# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = float('-inf')

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            current_split_sum = node.val + left_gain + right_gain

            self.max_path_sum = max(current_split_sum,  self.max_path_sum)

            return node.val + max(left_gain, right_gain)
        
        dfs(root)

        return self.max_path_sum 

        