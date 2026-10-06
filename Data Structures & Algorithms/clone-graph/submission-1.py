"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        hash_map = {}

        def dfs(curr_node: Optional['Node']):

            if curr_node in hash_map:
                return hash_map[curr_node]
            
            copy = Node(curr_node.val)

            hash_map[curr_node] = copy

            for neighbor in curr_node.neighbors:
                cloned_neighbor = dfs(neighbor)
                copy.neighbors.append(cloned_neighbor)
            
            return copy

        
        return dfs(node)
