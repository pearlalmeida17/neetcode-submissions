class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        hashmap = {i: [] for i in range(n) }
        for n1, n2 in  edges:
            hashmap[n1].append(n2)
            hashmap[n2].append(n1)
        
        visited = set()

        def dfs(node, parent):

            visited.add(node)

            for neighbor in hashmap[node]:

                if neighbor == parent:
                    continue
                
                if neighbor in visited:
                    return False
                
                if not dfs(neighbor, node):
                    return False
            
            return True
                
            for edge in hashmap[node]:
                dfs(edge)
            
            visited.remove(node)
            hashmap[node] = []

            return True
        
        if not dfs(0, -1):
            return False

        return len(visited) == n

        