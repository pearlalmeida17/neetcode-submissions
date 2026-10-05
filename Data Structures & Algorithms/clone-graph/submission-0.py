"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # Hash map to map original nodes to their cloned copies
        old_to_new = {}

        def dfs(curr_node):
            # If the node was already cloned, return the existing copy
            if curr_node in old_to_new:
                return old_to_new[curr_node]

            # Create a deep copy of the current node
            copy = Node(curr_node.val)
            old_to_new[curr_node] = copy

            # Recursively clone all neighbor nodes
            for neighbor in curr_node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)